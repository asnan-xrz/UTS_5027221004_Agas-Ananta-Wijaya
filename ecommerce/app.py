from flask import Flask, render_template, request, jsonify
import grpc
import product_pb2
import product_pb2_grpc

app = Flask(__name__)

def get_grpc_stub():
    channel = grpc.insecure_channel('localhost:50052') 
    stub = product_pb2_grpc.ProductServiceStub(channel)
    return stub

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products', methods=['GET'])
def products():
    stub = get_grpc_stub()
    response = stub.ListProducts(product_pb2.Empty())
    products = [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price} for product in response.products]
    return jsonify({'products': products})

@app.route('/product', methods=['POST'])
def create_product():
    data = request.json
    name = data['name']
    description = data['description']
    price = float(data['price'])
    product = product_pb2.Product(name=name, description=description, price=price)
    stub = get_grpc_stub()
    response = stub.CreateProduct(product)
    return jsonify({'success': True, 'message': 'Product created successfully'})

@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    data = request.json
    name = data['name']
    description = data['description']
    price = float(data['price'])
    product = product_pb2.Product(id=id, name=name, description=description, price=price)
    stub = get_grpc_stub()
    response = stub.UpdateProduct(product)
    return jsonify({'success': True, 'message': 'Product updated successfully'})

@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product_id = product_pb2.ProductId(id=id)
    stub = get_grpc_stub()
    response = stub.DeleteProduct(product_id)
    return jsonify({'success': True, 'message': 'Product deleted successfully'})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
