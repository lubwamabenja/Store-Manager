from flask import Flask, Blueprint,render_template, redirect,request,url_for,session,flash,jsonify,json
from flasgger import swag_from
from functools import wraps
from app.models.products import *
from app.models.sales import *


records = Blueprint('records', __name__)


@records.route('/v1/')
def home():
    return render_template("index.html")




@records.route('/v1/products', methods=['POST'])
@swag_from('../apidocs/products/create_product.yml')
def create_product():
    ''' function enables the attendant/admin to add products
    to the stock '''

    req_data = request.get_json()
    product = Products(req_data['prod_id'],req_data['prod_name'],
    req_data['prod_quantity'],req_data['prod_category'],
    req_data['unit_cost'])
    Products.products.append(product)
    return jsonify("Products has been added to the store"), 201
           





@records.route('/v1/products', methods=['GET'])
@swag_from('../apidocs/products/get_products.yml')
def return_all():
    ''' function enables the users to view all products
    and returns all products '''
    if len(Products.products) == 0:
        return jsonify({
            'message': 'There are not products yet!'
        }), 400
    return jsonify({
        'products': [product.__dict__ for product in Products.products]
    }), 200



@records.route('/v1/products/<int:prod_id>', methods=['GET'])
@swag_from('../apidocs/products/get_single_product.yml')
def return_uniq_product(prod_id):
    ''' function  returns a single product searched by Id '''
    try:
        if len(Products.products) == 0:
            return jsonify({
                'message': 'There are no products yet!'
            }), 404
        product = Products.products[prod_id - 1]
        return jsonify({
            'product': product.__dict__,
            'message': 'Product fetched!'
        }), 200
    except IndexError:
        return jsonify({
            'message': 'This product does not exist!'
        }), 404



@records.route('/v1/sales', methods=['POST'])
@swag_from('../apidocs/sales/create_sale_record.yml')
def add_sales():
    ''' this function enables the user to add sales to the stock '''
    req_data = request.get_json()
    sale_order = Sales(req_data['sale_id'],req_data['prod_name'],
    req_data['prod_quantity'],req_data['attendant'],
    req_data['price'])
    Sales.sales_records.append(sale_order)
    return jsonify("Order has been successfully placed"), 201
        



@records.route('/v1/sales', methods=['GET'])
@swag_from('../apidocs/sales/get_all_sales.yml')
def get_sales():
    '''function returns all sale records '''
    if len(Sales.sales_records) == 0:
        return jsonify({
            'message': 'No sales yet in stock!'
        }), 400
    return jsonify({
        'sales_records': [sale.__dict__ for sale in Sales.sales_records]
    }), 200



@records.route('/v1/sales/<int:sale_id>', methods=['GET'])
@swag_from('../apidocs/sales/get_single_sale.yml')
def return_uniq_sale(sale_id):
    ''' returns a single product in sale records '''
    try:
        if len(Sales.sales_records) == 0:
            return jsonify({
                'message': 'There are no sale records yet!'
            }), 404
        sale = Sales.sales_records[sale_id - 1]
        return jsonify({
            'sale_record': sale.__dict__,
            'message': 'sale record has been returned!'
        }), 200
    except IndexError:
        return jsonify({
            'message': 'This sale record does not exist!'
        }), 404



