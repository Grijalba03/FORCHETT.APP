import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from ..modelos import Categories, User
from flask import Flask, url_for
from datetime import datetime
import json 
from ..utils import APIException

@app.route('/profile/<string:username>', methods=['GET'])
def get_profile_by_username(username):
    print("username" + username)
    body = request.get_json()
    print("body" + body)
    if username=="":
        raise APIException("username cannot be empty", status_code=400)  
    if body['username'] is None:
        raise APIException("Username does not exist", status_code=400) 
    user = User.query.filter_by(username = username).first() 
    print(user.serialize())
    #validaciones
    if body is None:
     raise APIException("body is empty" , status_code=400)
    if not body['username'] is None:
     user.username = body['username']
     db.session.commit()     
    return jsonify(username.serialize()), 200   
     
