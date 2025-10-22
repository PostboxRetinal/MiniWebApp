from flask import Blueprint, request, jsonify
from users.models.product_model import Product
from users.models.db import db

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/api/products', methods=['GET'])
def get_products():
    print("listado de productos")
    products = Product.query.all()
    result = [{'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price} for product in products]
    return jsonify(result)

@product_controller.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    print("obteniendo producto")
    product = Product.query.get_or_404(product_id)
    return jsonify({'id': product.id, 'name': product.name, 'description': product.description, 'price': product.price})

@product_controller.route('/api/products', methods=['POST'])
def create_product():
    print("creando producto")
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    if 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Name and price are required'}), 400
    new_product = Product(name=data['name'], description=data.get('description'), price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

@product_controller.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    print("actualizando producto")
    product = Product.query.get_or_404(product_id)
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

@product_controller.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})