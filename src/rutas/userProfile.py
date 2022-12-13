import os
from ..main import request, jsonify, app, bcrypt, jwt_required, create_access_token, get_jwt_identity, get_jwt
from ..db import db
from ..modelos import Categories, User, Recipe
from flask import Flask, url_for
from datetime import datetime
import json 
from ..utils import APIException


@app.route('/profile/<string:username>', methods=['GET'])
#@jwt_required() 
def get_profile_by_username(username):
    
    # print("username" ,username())
   
    if username=="":
        raise APIException("username cannot be empty", status_code=400)  
    user = User.query.filter_by(username = username).first() 
    submittedRecipes = Recipe.query.filter(Recipe.username==user.username).all()
    submittedRecipes = list(map(lambda item: item.serialize(), submittedRecipes))
    #submittedRecipes = Recipe.query.filter_by(username = username).order_by(Recipe.title).all()
    #submittedRecipes = Recipe.query(username).filter(Recipe.title.in_([username]))
    # submittedRecipes = Recipe.query(username).filter_by(Recipe.title()).all()

    print(user)
    #print("tus recipes",submittedRecipes)
    
    #validaciones
    # if body is None:
    #  raise APIException("body is empty" , status_code=400)
    # if not body['username'] is None:
    # user.username = body['username'] 
    userInfo = { "username":user.username, 
                "image":user.image,
                "title":user.title,
                "dietaryPreferences":user.dietaryPreferences,
                "facebook":user.facebook,
                "instagram":user.instagram,
                "youtube":user.youtube,
                "twitter":user.twitter,
                "submittedRecipes":submittedRecipes
    } 
     
   
    
           
         
    #return jsonify({userInfo}), 200   
    return jsonify(userInfo), 200   

   
    
     
