from flask import Flask, render_template, redirect,request,url_for,session,flash,jsonify,json
from functools import wraps
from app import app
from app.models.models import *


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

product_data = Products()
sales_data = Sales()

@app.route('/')
@login_required
def home():
	return render_template("index.html")


@app.route('/welcome')
def welcome():
	return render_template("welcome.html")

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
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
@app.route('/v1/products',methods=['POST'])
#@login_required
def add_product():
    product={
            'prod_id':request.json['prod_id'],
            'prod_name':request.json['prod_name'],
            'prod_category':request.json['prod_category'],
            'prod_quantity': request.json['prod_quantity'],
            'unit_cost': request.json['unit_cost']
        }

    products.append(product)
    return jsonify({'products' : products})



''' this route returns all the sales records made  by the attendant '''
@app.route('/v1/sales',methods=['GET'])
@login_required
def get_sales():
    return jsonify(sales)


@app.route('/v1/sales/<int:id>',methods=['GET'])
@login_required
def return_uniq_sale(id):
	id = [sale for sale in sales if sale['sale_id'] == id]
	return jsonify ({'product' : id[0]})

 
#This route enables attendant/owner to add sales
@app.route('/v1/sales',methods=['POST'])
#@login_required
def add_sales():
    return sales_data.add_sales()
    


@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('welcome'))