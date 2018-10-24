from flask import Flask, render_template, redirect,request,url_for,session,flash,jsonify,json
from functools import wraps
from app import app
from app.views.views import *
from app.models.products import *
from app.models.sales import *


app.secret_key = 'my precious'



""" login required decorator """
def login_required(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))

	return wrap
    

@app.route('/v1/')
#@login_required
def home():
	return render_template("index.html")

# Route for handling the login page logic
@app.route('/v1/login', methods=['GET', 'POST'])
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



@app.route('/v1/products',methods=['GET'])
def return_all():
    return jsonify(products)

@app.route('/v1/products/<int:id>',methods=['GET'])
def return_uniq_product(id):
    id = [product for product in products if product['prod_id'] == id]
    return jsonify ({'product' : id[0]})

 
""" This route enables attendant/owner to add products """
@app.route('/v1/products/create',methods=['POST'])
@login_required
def add_product():
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



''' this route returns all the sales records made  by the attendant '''
@app.route('/v1/sales',methods=['GET'])
@login_required
def get_sales():
    return jsonify(sales)


''' this route returns a unique sale by id ''' 
@app.route('/v1/sales/<int:id>',methods=['GET'])
@login_required
def return_uniq_sale(id):
	id = [sale for sale in sales if sale['sale_id'] == id]
	return jsonify ({'product' : id[0]})

 
#This route enables attendant/owner to add sales
@app.route('/v1/sales/create',methods=['POST'])
@login_required
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

    

''' this route enables the user to logout '''
@app.route('/v1/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('welcome'))
