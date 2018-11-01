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
	db.cur.execute("SELECT * FROM Products")
	products = db.cur.fetchall()

	if not products:
		return jsonify({'message': 'No products have been added to the database'})

	return jsonify({'products' : products})


@product.route('/v2/products',methods=['POST'])
@jwt_required
def create_products():
	data = request.get_json()
	prod_name = data['prod_name']
	prod_quantity = data['prod_quantity']
	unit_cost = data['unit_cost']
	category_name = data['category_name']

	db.cur.execute("INSERT INTO Products(prod_name,prod_quantity,unit_cost,category_name)\
		           VALUES (%s,%s,%s,%s)",(prod_name,prod_quantity,unit_cost,category_name))

	return jsonify({'message' : "product has been created"})





@product.route('/v2/products/<prod_id>',methods=['GET'])
@jwt_required
def get_one_product_by_id(prod_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	sql = """SELECT * FROM Products WHERE prod_id = %s"""
	db.cur.execute(sql,(prod_id))
	product = db.cur.fetchone()
	if not products:
		return jsonify({'message' : 'No product found!'})
	return jsonify({'products':product})




	

@product.route('/v2/products/<int:prod_id>',methods=['PUT'])
@jwt_required
def modify_product(prod_id):

	db.cur.execute("SELECT * FROM Products WHERE prod_id = prod_id")
	product = db.cur.fetchone()
	if not product:
		return jsonify({'message' : 'No product found!'})

	data = request.get_json()
	prod_name = data['prod_name']
	db.cur.execute("UPDATE Users SET  prod_name= %s  WHERE user_id=user_id",(prod_name))


	return jsonify({'message':'Product has been modified'})




@product.route('/v2/products/<prod_id>',methods=['DELETE'])
@jwt_required
def delete_product(prod_id):

	db.cur.execute("SELECT * FROM Products WHERE prod_id = prod_id")
	product = db.cur.fetchone()
	if not product:
		return jsonify({'message' : 'No product found!'})
	
	db.cur.execute("DELETE FROM Products WHERE prod_id = prod_id")
	return jsonify({'message':'Product has been deleted'})

