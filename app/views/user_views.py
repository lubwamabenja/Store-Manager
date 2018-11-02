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



user = Blueprint('user', __name__)
 
db = MyDatabase()



@user.route('/v2/users',methods=['POST'])
def create_user():
		user = request.get_json()
		hashed_password = generate_password_hash(user['password'],method='sha256')
		username = user['username']
		password = user['password']
		if not username or not isinstance(username,str) or username.isspace() :
			return jsonify({'message':'username should be a string and of length greater than 5'})
		
		elif not password or not isinstance(password,str) or not len(password)> 6 :
			return jsonify({'message':'password should be a string and of length greater than 5'})

		elif  db.select('Users','username',username):
			return jsonify({'message':'username already exists'})

		
		db.cur.execute("INSERT INTO Users(username,password,admin) \
		VALUES(%s,%s,False)",(username,hashed_password))
		return jsonify({'message': 'New user created!'})


@user.route('/v2/users',methods=['GET'])
@jwt_required
def get_all_users():
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select_all('Users'):
		return jsonify({'users' : 'There are no users in the database'})

	records = db.select_all('Users')
	return jsonify({'Users':records})

	

	


@user.route('/v2/users/<user_id>', methods=['GET'])
@jwt_required
def get_one_user(user_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select('Users','user_id',user_id):
		return jsonify({'message' : 'No user found!'})
	user = db.select('Users','user_id',user_id)
	return jsonify({'user': user})


@user.route('/v2/users/<user_id>',methods=['PUT'])
@jwt_required
def promote_user(user_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select('Users','user_id',user_id):
		return jsonify({'message' : 'No user found!'})
	elif  db.select('Users','admin','true'):
			return jsonify({'message':'person already an admin'})

	db.update('Users','admin','true' ,'user_id',user_id)
	return jsonify({'message':'Attendant has been assigned user rights'})


@user.route('/v2/users/demote/<user_id>',methods=['PUT'])
@jwt_required
def demote_user(user_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select('Users','user_id',user_id):
		return jsonify({'message' : 'No user found!'})
	elif  db.select('Users','admin','false'):
			return jsonify({'message':'person already an attendant'})
	db.update('Users','admin','false' ,'user_id',user_id)
	return jsonify({'message':'Attendant has been demoted'})


@user.route('/v2/users/<user_id>', methods=['DELETE'])
@jwt_required
def delete_user(user_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select('Users','user_id',user_id):
		return jsonify({'message' : 'No user found!'})
	elif  db.select('Users','admin','true'):
			return jsonify({'message':'you cannot delete an admin'})
	response = db.delete('Users','user_id',user_id)
	return jsonify({'attendant has been deleted'})

	

@user.route('/v2/users', methods=['DELETE'])
@jwt_required
def delete_users():
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	elif not db.select_all('Users'):
		return jsonify({'users' : 'There are no users in the database'})
	
	response = db.delete_all('Users','admin','false')
	return jsonify({'message':'Attendants have been deleted but you cant delete an admin'})
