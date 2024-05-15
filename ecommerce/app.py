from flask import Flask, render_template, request, jsonify
from concurrent import futures
import grpc
import product_pb2
import product_pb2_grpc
import product_service
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Start gRPC server
def start_grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(product_service.ProductServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products', methods=['GET'])
def products():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = product_pb2_grpc.ProductServiceStub(channel)
        response = stub.ListProducts(product_pb2.Empty())
    products = [{"id": p.id, "name": p.name, "description": p.description, "price": p.price} for p in response.products]
    return jsonify({"products": products})

@app.route('/product', methods=['POST'])
def create_product():
    data = request.json
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = product_pb2_grpc.ProductServiceStub(channel)
        product = product_pb2.Product(name=data['name'], description=data['description'], price=data['price'])
        response = stub.CreateProduct(product)
    return jsonify({"success": response.success, "message": response.message, "product": {"id": response.product.id, "name": response.product.name, "description": response.product.description, "price": response.product.price}})

@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    data = request.json
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = product_pb2_grpc.ProductServiceStub(channel)
        product = product_pb2.Product(id=id, name=data['name'], description=data['description'], price=data['price'])
        response = stub.UpdateProduct(product)
    return jsonify({"success": response.success, "message": response.message})

@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = product_pb2_grpc.ProductServiceStub(channel)
        product_id = product_pb2.ProductId(id=id)
        response = stub.DeleteProduct(product_id)
    return jsonify({"success": response.success, "message": response.message})

if __name__ == "__main__":
    import threading
    grpc_thread = threading.Thread(target=start_grpc_server)
    grpc_thread.start()
    app.run(port=5000, debug=True)
