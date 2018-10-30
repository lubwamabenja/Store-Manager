from flask import Flask, Blueprint,render_template, redirect,request,url_for,session,flash,jsonify,json
from flasgger import swag_from
from functools import wraps
import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from functools import wraps


from app.models.database import *



user = Blueprint('user', __name__)
 
db = MyDatabase()





@user.route('/v1/users',methods=['POST'])
#@token_required
def create_user():
	user = request.get_json()
	hashed_password = generate_password_hash(user['password'],method='sha256')
	username = user['username']
	password = user['password']
	db.cur.execute("INSERT INTO Users(username,password,admin) \
	VALUES(%s,%s,False)",(username,hashed_password))
	return jsonify({'message': 'New user created!'})

@user.route('/v1/users',methods=['GET'])
#@token_required
def get_all_users():
	#if not current_user.admin:
		#return jsonify({'message':'cannot perform that role '})
	db.cur.execute("SELECT * FROM Users")
	users = db.cur.fetchall()
	if not users:
		return jsonify({'message' : 'No users found!'})

	return jsonify({'users' : users})


@user.route('/v1/users/<user_id>', methods=['GET'])
#@token_required
def get_one_user(user_id):
	db.cur.execute("SELECT * FROM Users WHERE user_id = user_id ")
	user = db.cur.fetchone()
	if not user:
		return jsonify({'message' : 'No user found!'})
	
	return jsonify({'user': user})


@user.route('/v1/users/<user_id>',methods=['PUT'])
#@token_required
def promote_user(user_id):
	db.cur.execute("SELECT * FROM Users WHERE user_id = user_id")
	user = db.cur.fetchone()
	if not user:
		return jsonify({'message' : 'No user found!'})

	db.cur.execute("UPDATE  Users SET admin = True WHERE user_id = user_id")

	return jsonify({'message':'Attendant has been assigned user rights'})


@user.route('/v1/users/<user_id>', methods=['DELETE'])
#@token_required
def delete_user(user_id):
	db.cur.execute("SELECT * FROM Users WHERE user_id = user_id")
	user = db.cur.fetchone()
	
	if not user:
		return jsonify({'message' : 'No user found!'})

	db.cur.execute("DELETE  FROM Users WHERE user_id = user_id ")
	return jsonify({'message': 'User has been deleted'})
