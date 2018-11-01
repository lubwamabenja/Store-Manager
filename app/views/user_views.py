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
	try:
		current_user = get_jwt_identity()
		if not current_user:
			return jsonify({'message':'you are not logged in yet'})

		user = request.get_json()
		hashed_password = generate_password_hash(user['password'],method='sha256')
		username = user['username']
		password = user['password']
		db.cur.execute("INSERT INTO Users(username,password,admin) \
		VALUES(%s,%s,False)",(username,hashed_password))
		return jsonify({'message': 'New user created!'})
	except:
		response ={'message':'user already exists'}
		return make_response(jsonify(response)),202


@user.route('/v2/users',methods=['GET'])
@jwt_required
def get_all_users():
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	db.cur.execute("SELECT * FROM Users")
	users = db.cur.fetchall()
	if not users:
		return jsonify({'message' : 'No users found!'})

	return jsonify({'users' : users})


@user.route('/v2/users/<user_id>', methods=['GET'])
@jwt_required
def get_one_user(user_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
	db.cur.execute("SELECT * FROM Users WHERE user_id = user_id ")
	user = db.cur.fetchone()
	if not user:
		return jsonify({'message' : 'No user found!'})
	
	return jsonify({'user': user})


@user.route('/v2/users/<user_id>',methods=['PUT'])
@jwt_required
def promote_user(user_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})

	db.cur.execute("SELECT * FROM Users WHERE user_id = user_id")
	user = db.cur.fetchone()
	if not user:
		return jsonify({'message' : 'No user found!'})

	db.cur.execute("UPDATE  Users SET admin = True WHERE user_id = user_id")

	return jsonify({'message':'Attendant has been assigned user rights'})


@user.route('/v2/users/<user_id>', methods=['DELETE'])
@jwt_required
def delete_user(user_id):
	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({'message':'you are not logged in yet'})
		
	db.cur.execute("SELECT * FROM Users WHERE user_id = user_id")
	user = db.cur.fetchone()
	
	if not user:
		return jsonify({'message' : 'No user found!'})

	db.cur.execute("DELETE  FROM Users WHERE user_id = user_id ")
	return jsonify({'message': 'User has been deleted'})
