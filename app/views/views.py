from flask import Flask, Blueprint,render_template, redirect,request,url_for,session,flash,jsonify,json
from flasgger import swag_from
from functools import wraps
from app.models.products import *
from app.models.sales import * 




records = Blueprint('records', __name__)
records.secret_key = 'my precious'




@records.route('/v1/')
#@login_required
def home():
    return render_template("index.html")

# Route for handling the login page logic
@records.route('/v1/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in!')
            return redirect(url_for('home'))
                
    return render_template('login.html', error=error)



@records.route('/v1/products', methods=['POST'])
@swag_from('../apidocs/products/create_product.yml')
def create_product():
    prod_data = json.loads(request.data.decode('utf-8'))
    product = {
            'prod_id':prod_data['self.prod_id'],
            'prod_name':prod_data['self.prod_name'],
            'prod_category':prod_data['self.prod_category'],
            'prod_quantity': prod_data['self.prod_quantity'],
            'unit_cost': prod_data['self.unit_cost']
        }

    products.append(product)
    return jsonify({'products' : products})
    return jsonify({"message": "Product successfully created"}), 201


@records.route('/v1/products', methods=['GET'])
@swag_from('../apidocs/products/get_products.yml')
def return_all():
    return jsonify(products)


@records.route('/v1/products/<int:id>', methods=['GET'])
@swag_from('../apidocs/products/get_single_product.yml')
def return_uniq_product(id):
    id = [product for product in products if product['prod_id'] == id]
    return jsonify ({'product' : id[0]})



@records.route('/v1/sales', methods=['POST'])
@swag_from('../apidocs/sales/create_sale_record.yml')
def add_sales():
    ''' function adds sale records to store '''
    req_data = json.loads(request.data.decode('utf-8'))
    sale_order = {
        'sale_id':req_data['self.sale_id'],
        'prod_name':req_data['self.prod_name'],
        'prod_quantity':req_data['self.prod_quantity'],
        'attendant':req_data['self.attendant'],
        'price':req_data['self.price']}
    sales.append(sale_order)
    return jsonify(sales)
    return jsonify({"message": "record created successfully"}), 201

@records.route('/v1/sales', methods=['GET'])
@swag_from('../apidocs/sales/get_all_sales.yml')
def get_sales():
    return jsonify(sales)


@records.route('/v1/sales/<int:id>', methods=['GET'])
@swag_from('../apidocs/sales/get_single_sale.yml')
def return_uniq_sale(id):
    id = [sale for sale in sales if sale['sale_id'] == id]
    return jsonify ({'product' : id[0]})




