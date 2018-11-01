from flask import Flask, Blueprint,render_template, redirect,request,url_for,session,flash,jsonify,json,make_response
from flasgger import swag_from
from functools import wraps
import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_jwt_extended import (create_access_token,get_jwt_identity, jwt_required)


from app.models.database import *
get_token = Blueprint('get_token', __name__)
 
db = MyDatabase()




@get_token.route('/auth/login', methods=['POST'])
def login():
    user = request.get_json()
    username = user['username']
    db.cur.execute("SELECT username,password FROM Users WHERE username=%s",[username])
    db_user = db.cur.fetchone()
    if not db_user:
    	return jsonify({'message':'No user found'})

    if not check_password_hash(db_user[1], user['password']):
    	return jsonify({'message':'Invalid password'})

    else:
    	access_token = create_access_token(identity=username)
    	return jsonify({'message':'successfully logged in',
        'token': access_token
    	}), 200
