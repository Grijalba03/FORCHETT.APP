import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from ..modelos import Categories 
from flask import Flask, url_for
from datetime import datetime
import json 

@app.route('/<string:username>', methods=['GET'])
def get_profile_by_username(username):
    print("username" + username)
    body = request.get_json()
    print("body" + body)
    if username=="":
        raise APIException("username no existe", status_code=400)  
    if body['username'] is None:
        raise APIException("El nombre de usuario no existe", status_code=400) 
    user = User.query.filter_by(username = username).first()
    # print(user)
    #validaciones
    # if body is None:
    #     raise APIException("Body está vacío" , status_code=400)
    # #validamos si viene el campo name en el body o no (despues de hacer el request.get_json())
    # if not body['username'] is None:
    #     user.username = body['username']
    # db.session.commit()     
    # return jsonify(username.serialize()), 200   #POR QUE ESTA LINEA SE SEREA;IZA ASI?  
    return "HI", 200   #POR QUE ESTA LINEA SE SEREA;IZA ASI?  
