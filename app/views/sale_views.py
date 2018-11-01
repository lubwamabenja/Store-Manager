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

sale = Blueprint('sale', __name__)

db = MyDatabase()



@sale.route('/v2/sales',methods=['GET'])
@jwt_required
def get_all_sales():
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	db.cur.execute("SELECT * FROM Sales")
	sales = db.cur.fetchall()

	if not sales:
		return jsonify({'message': 'No sales have been added to the database'})

	return jsonify({'sales' : sales})






@sale.route('/v2/sales',methods=['POST'])
@jwt_required
def create_sales():
	try:

		current_user = get_jwt_identity()
		if not current_user:
			return jsonify({'message':'you are not logged in yet'})
		
		data = request.get_json()
		prod_name = data['prod_name']
		prod_quantity = data['prod_quantity']
		db.cur.execute("SELECT unit_cost,prod_quantity FROM Products WHERE prod_name = %s",[prod_name])
		details = db.cur.fetchone()
		total_cost = prod_quantity * details[0]
		if details[1] < prod_quantity:
			return jsonify({'message':'products are less in stock'})
		else:
			balance = details[1] - prod_quantity
		sql = """UPDATE Products SET prod_quantity= %s WHERE prod_name = %s"""
		db.cur.execute(sql,(balance,prod_name))
		db.cur.execute("INSERT INTO Sales(prod_name,prod_quantity)\
		VALUES (%s,%s)",(prod_name,prod_quantity))
		return jsonify({'message' : "sale has been created" ,'total_cost':total_cost}),201

	except:
		return jsonify({'message':'product is not in stock'})







@sale.route('/v2/sales/<sale_id>',methods=['GET'])
@jwt_required
def get_one_sale_by_id(sale_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	sql = """SELECT * FROM Sales WHERE sale_id = %s"""
	db.cur.execute(sql,(sale_id))
	sale = db.cur.fetchone()
	if not sale:
		return jsonify({'message' : 'No sale found!'})
	return jsonify({'sales':sale})

			

@sale.route('/v2/sales/<sale_id>',methods=['PUT'])
@jwt_required
def modify_sale(sale_id):
	try:
		current_user = get_jwt_identity()
		if not current_user:
			return jsonify({'message':'you are not logged in yet'})
		sql = """SELECT * FROM Sales WHERE sale_id = %s"""
		db.cur.execute(sql,(sale_id))
		sale = db.cur.fetchone()
		if not sale:
			return jsonify({'message' : 'No sale found!'})

		data = request.get_json()
		prod_name = data['prod_name']
		prod_quantity = data['prod_quantity']
		sql ="""UPDATE Sales SET  prod_name = %s,prod_quantity = %s  WHERE sale_id = %s"""
		db.cur.execute(sql,(prod_name,prod_quantity,sale_id))
		return jsonify({'message':'sale has been modified'})
	except:
		return jsonify({'message':'replacement product name is not in products table'})






@sale.route('/v2/sales/<sale_id>',methods=['DELETE'])
@jwt_required
def delete_sale(sale_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})

	db.cur.execute("SELECT * FROM Sales WHERE sale_id = sale_id")
	sale = db.cur.fetchone()
	if not sale:
		return jsonify({'message' : 'No sale found!'})
	
	db.cur.execute("DELETE FROM Sales WHERE sale_id= sale_id")
	return jsonify({'message':'sale has been deleted'})

