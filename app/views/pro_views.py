from flask import Flask, Blueprint,render_template, redirect,request,url_for,session,flash,jsonify,json,make_response
from flasgger import swag_from
from functools import wraps
import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_jwt_extended import (create_access_token,get_jwt_identity, jwt_required)
from app.models.login import *
from app.models.database import *

product = Blueprint('product', __name__)

db = MyDatabase()



@product.route('/v2/products',methods=['GET'])
@jwt_required
def get_all_products():
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select_all('Products'):
		return jsonify({'users' : 'There are no products in the database'})
	products =db.select_all('Products')
	return jsonify({'products' : products})


@product.route('/v2/products',methods=['POST'])
@jwt_required
def create_products():
	data = request.get_json()
	prod_name = data['prod_name']
	prod_quantity = data['prod_quantity']
	unit_cost = data['unit_cost']
	category_name = data['category_name']
	if not prod_name or not isinstance(prod_name,str) or prod_name.isspace() :
			return jsonify({'message':'prod_name should be a string and should no be empty'})
		
	elif not prod_quantity or not isinstance(prod_quantity,int):
			return jsonify({'message':'prod_quantity should be an integer and not empty'})

	elif not unit_cost or not isinstance(unit_cost,int):
			return jsonify({'message':'unit_cost should be an integer and not empty'})
	elif not category_name or not isinstance(category_name,str):
			return jsonify({'message':'category_name should be a string and should no be empty'})

	elif  db.select('Products','prod_name',prod_name):
			return jsonify({'message':'product already exists'})

	db.cur.execute("INSERT INTO Products(prod_name,prod_quantity,unit_cost,category_name)\
		           VALUES (%s,%s,%s,%s)",(prod_name,prod_quantity,unit_cost,category_name))

	return jsonify({'message' : "product has been created"})





@product.route('/v2/products/<prod_id>',methods=['GET'])
@jwt_required
def get_one_product_by_id(prod_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select('Products','prod_id',prod_id):
		return jsonify({'message' : 'No product found!'})
	product = db.select('Products','prod_id',prod_id)
	return jsonify({'product':product })





	

@product.route('/v2/products/<int:prod_id>',methods=['PUT'])
@jwt_required
def modify_product(prod_id):
	data = request.get_json()
	prod_name = data['prod_name']
	prod_quantity = data['prod_quantity']
	unit_cost = data['unit_cost']
	category_name = data['category_name']
	if not prod_name or not isinstance(prod_name,str) or prod_name.isspace() :
			return jsonify({'message':'prod_name should be a string and should no be empty'})
		
	elif not prod_quantity or not isinstance(prod_quantity,int):
			return jsonify({'message':'prod_quantity should be an integer and not empty'})

	elif not unit_cost or not isinstance(unit_cost,int):
			return jsonify({'message':'unit_cost should be an integer and not empty'})
	elif not category_name or not isinstance(category_name,str):
			return jsonify({'message':'category_name should be a string and should no be empty'})

	elif  db.select('Products','prod_name',prod_name):
			return jsonify({'message':'product with that name  already exists'})

	db.cur.execute("UPDATE Products SET {} ='{}',{} ='{}',{} ='{}',{} ='{}'\
		           WHERE {} = {}".format('prod_name',prod_name,'prod_quantity',prod_quantity,\
		           	'unit_cost',unit_cost,'category_name',category_name,'prod_id',prod_id))

	return jsonify({'message':'Product has been modified'})




@product.route('/v2/products/<prod_id>',methods=['DELETE'])
@jwt_required
def delete_product(prod_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select('Products','prod_id',prod_id):
		return jsonify({'message' : 'No product found!'})
	response = db.delete('Products','prod_id',prod_id)
	return jsonify({'message','product has been deleted'})
