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

category = Blueprint('category', __name__)

db = MyDatabase()



@category.route('/v2/categories',methods=['GET'])
@jwt_required
def get_all_categories():
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select_all('Categories'):
		return jsonify({'categories' : 'There are no categories in the database'})
	categories =db.select_all('Categories')
	return jsonify({'categories' : categories})


@category.route('/v2/categories',methods=['POST'])
@jwt_required
def create_categoriess():
	data = request.get_json()
	category_name = data['category_name']
	if not category_name or not isinstance(category_name,str) or category_name.isspace() :
			return jsonify({'message':'category should be a string and should no be empty'})

	elif  db.select('Categories','category_name',category_name):
			return jsonify({'message':'category already exists'})

	sql ="""INSERT INTO Categories({}) \
		           VALUES ('{}')""".format('category_name',category_name)
	db.cur.execute(sql)

	return jsonify({'message' : "category has been created"})


@category.route('/v2/categories/<category_id>',methods=['GET'])
@jwt_required
def get_one_category_by_id(category_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select('Categories','category_id',category_id):
		return jsonify({'message' : 'No category found!'})
	category = db.select('Categories','category_id',category_id)
	return jsonify({'category':category })


@category.route('/v2/categories/<category_id>',methods=['DELETE'])
@jwt_required
def delete_category(category_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select('Categories','category_id',category_id):
		return jsonify({'message' : 'No category found!'})
	response = db.delete('Categories','category_id',category_id)
	return jsonify({'message','category  has been deleted'})



@category.route('/v2/categories/<category_id>',methods=['PUT'])
@jwt_required
def modify_categories(category_id):
	data = request.get_json()
	category_name = data['category_name']
	if not category_name or not isinstance(category_name,str) or category_name.isspace() :
			return jsonify({'message':'category should be a string and should no be empty'})

	elif  db.select('Categories','category_name',category_name):
			return jsonify({'message':'category already exists'})

	db.cur.execute("UPDATE Categories SET {} ='{}'\
		           WHERE {} = {}".format('category_name',category_name,'category_id',category_id))

	return jsonify({'message':'category has been modified'})



@category.route('/v2/categories/add/<category_id>',methods=['PUT'])
@jwt_required
def add_products(category_id):
	data = request.get_json()
	prod_name = data['prod_name']
	if not prod_name or not isinstance(prod_name,str) or prod_name.isspace() :
		return jsonify({'message':'category should be a string and should no be empty'})

	elif  not  db.select('Products','prod_name',prod_name):
		return jsonify({'message':'product does not exist in products'}
			)
	elif  db.select('Categories','prod_name',prod_name):
		return jsonify({'message':'product already exists in get_all_categoriess'})

	db.cur.execute("UPDATE Categories SET {} ='{}'\
		           WHERE {} = {}".format('prod_name',prod_name,'category_id',category_id))

	return jsonify({'message':'product has been added'})