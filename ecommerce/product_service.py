import product_pb2
import product_pb2_grpc
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']
collection = db['products']

class ProductServiceServicer(product_pb2_grpc.ProductServiceServicer):
    def CreateProduct(self, request, context):
        product = {
            "name": request.name,
            "description": request.description,
            "price": request.price
        }
        result = collection.insert_one(product)
        product["id"] = str(result.inserted_id)
        return product_pb2.ProductResponse(success=True, message="Product created", product=product_pb2.Product(**product))

    def GetProduct(self, request, context):
        product = collection.find_one({"_id": ObjectId(request.id)})
        if product:
            product["id"] = str(product["_id"])
            return product_pb2.ProductResponse(success=True, message="Product found", product=product_pb2.Product(**product))
        else:
            return product_pb2.ProductResponse(success=False, message="Product not found")

    def UpdateProduct(self, request, context):
        query = {"_id": ObjectId(request.id)}
        new_values = {"$set": {"name": request.name, "description": request.description, "price": request.price}}
        result = collection.update_one(query, new_values)
        if result.matched_count > 0:
            return product_pb2.ProductResponse(success=True, message="Product updated", product=request)
        else:
            return product_pb2.ProductResponse(success=False, message="Product not found")

    def DeleteProduct(self, request, context):
        result = collection.delete_one({"_id": ObjectId(request.id)})
        if result.deleted_count > 0:
            return product_pb2.ProductResponse(success=True, message="Product deleted")
        else:
            return product_pb2.ProductResponse(success=False, message="Product not found")

    def ListProducts(self, request, context):
        products = collection.find()
        product_list = []
        for product in products:
            product["id"] = str(product["_id"])
            product_list.append(product_pb2.Product(**product))
        return product_pb2.ProductList(products=product_list)