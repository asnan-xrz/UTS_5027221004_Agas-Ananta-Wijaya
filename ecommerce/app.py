from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']
products_collection = db['products']

def fetch_products():
    products = list(products_collection.find({}))
    return [{'id': str(product['_id']), 'name': product['name'], 'description': product['description'], 'price': product['price']} for product in products]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products', methods=['GET'])
def get_products():
    products = fetch_products()
    return jsonify({'products': products})

@app.route('/product', methods=['POST'])
def create_product():
    data = request.json
    name = data['name']
    description = data['description']
    price = float(data['price'])
    product_id = products_collection.insert_one({'name': name, 'description': description, 'price': price}).inserted_id
    return jsonify({'success': True, 'message': 'Product created successfully', 'id': str(product_id)})

@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    data = request.json
    name = data['name']
    description = data['description']
    price = float(data['price'])
    products_collection.update_one({'_id': ObjectId(id)}, {'$set': {'name': name, 'description': description, 'price': price}})
    return jsonify({'success': True, 'message': 'Product updated successfully'})

@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    products_collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'success': True, 'message': 'Product deleted successfully'})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
