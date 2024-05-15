import uuid
from concurrent import futures
import grpc
import product_pb2
import product_pb2_grpc

products_db = {}

class ProductServiceServicer(product_pb2_grpc.ProductServiceServicer):
    def CreateProduct(self, request, context):
        product_id = str(uuid.uuid4())
        product = product_pb2.Product(id=product_id, name=request.name, description=request.description, price=request.price)
        products_db[product_id] = product
        return product_pb2.Empty()

    def UpdateProduct(self, request, context):
        if request.id in products_db:
            product = products_db[request.id]
            product.name = request.name
            product.description = request.description
            product.price = request.price
            products_db[request.id] = product
            return product_pb2.Empty()
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Product not found')
            return product_pb2.Empty()

    def DeleteProduct(self, request, context):
        if request.id in products_db:
            del products_db[request.id]
            return product_pb2.Empty()
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Product not found')
            return product_pb2.Empty()

    def ListProducts(self, request, context):
        response = product_pb2.ProductList()
        for product in products_db.values():
            response.products.append(product)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductServiceServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("gRPC server started on port 50052")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
