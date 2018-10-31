from flask import Flask, Blueprint,render_template, redirect,request,url_for,session,flash,jsonify,json,make_response
from flasgger import swag_from
from functools import wraps
import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_jwt_extended import (create_access_token,get_jwt_identity, jwt_required)

from app.models.database import *

sale = Blueprint('sale', __name__)

db = MyDatabase()



@sale.route('/v2/sales',methods=['GET'])
#@token_required
def get_all_sales():
	db.cur.execute("SELECT * FROM Sales")
	sales = db.cur.fetchall()

	if not sales:
		return jsonify({'message': 'No sales have been added to the database'})

	return jsonify({'sales' : sales})


@sale.route('/v2/sales',methods=['POST'])
#@token_required
def create_sales():
	data = request.get_json()
	prod_id = data['prod_id']
	prod_name = data['prod_name']
	unit_cost = data['unit_cost']
	prod_quantity = data['prod_quantity']
	db.cur.execute("INSERT INTO Sales(prod_id,prod_name,unit_cost,prod_quantity)\
		           VALUES (%s,%s,%s,%s)",(prod_id,prod_name,unit_cost,prod_quantity))

	return jsonify({'message' : "sale has been created"})

@sale.route('/v2/sales/<sale_id>',methods=['GET'])
#@token_required
def get_one_sale(sale_id):
	db.cur.execute("SELECT * FROM Sales WHERE sale_id = sale_id")
	sale = db.cur.fetchone()
	if not sale:
		return jsonify({'message' : 'No sale found!'})
	
	return jsonify({'sale':sale})
	

@sale.route('/v2/sales/<sale_id>',methods=['PUT'])
#@token_required
def modify_sale(sale_id):

	db.cur.execute("SELECT * FROM Sales WHERE sale_id = sale_id")
	sale = db.cur.fetchone()
	if not sale:
		return jsonify({'message' : 'No sale found!'})

	data = request.get_json()
	prod_name = data['prod_name']
	db.cur.execute("UPDATE Users SET  prod_name = %s  WHERE sale_id =sale_id",(prod_name))


	return jsonify({'message':'sale has been modified'})

@sale.route('/v2/sales/<sale_id>',methods=['DELETE'])
#@token_required
def delete_sale(sale_id):

	db.cur.execute("SELECT * FROM Sales WHERE sale_id = sale_id")
	sale = db.cur.fetchone()
	if not sale:
		return jsonify({'message' : 'No sale found!'})
	
	db.cur.execute("DELETE FROM Sales WHERE sale_id= sale_id")
	return jsonify({'message':'sale has been deleted'})

