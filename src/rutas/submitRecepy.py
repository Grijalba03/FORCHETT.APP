import os
from ..main import request, jsonify, app, jwt_required, get_jwt_identity, get_jwt
from ..db import db
from ..modelos import Recipe, User, Blocked
from flask import Flask, url_for
import json
from ..utils import APIException


@app.route('/submit', methods=['POST'])
@jwt_required()
def create_new_recipe():
    userId = get_jwt_identity()
    jti = get_jwt()['jti']
    foundtoken = Blocked.query.filter_by(blocked_token=jti).first()
    if not foundtoken is None:
        raise APIException("Token has already expired or invalid.", status_code=400)

    user = User.query.get(userId)
    userName = user.serialize()['username']
    print("user: ", userName)
    body = request.get_json()

    if body is None:
        raise APIException("Body está vacío" , status_code=400)
    
    if body['title'] is None or body['title']=="":
        raise APIException("Name cannot be empty!" , status_code=400)
    if body['category'] is None or body['category']=="":
        raise APIException("Select a category" , status_code=400)
    if body['prep'] is None or body['prep']=="":
        raise APIException("prep cannot be empty!" , status_code=400)
    if body['preparation'] is None or body['preparation']=="":
        raise APIException("preparation cannot be empty!" , status_code=400)
    if body['ingredients'] is None or body['ingredients']=="":
        raise APIException("ingredients cannot be empty!" , status_code=400)
    if body['description'] is None or body['description']=="":
        raise APIException("description cannot be empty!" , status_code=400)
    if body['image'] is None or body['image']=="":
        image = ""
    if body['bake'] is None or body['bake']=="":
        bake = ""

    new_recipe = Recipe(username=userName, category=body['category'], title=body['title'], servings=body['servings'], 
    prep=body['prep'], bake=body['bake'], preparation=body['preparation'], ingredients=body['ingredients'], 
    description=body['description'], image=body['image'])

    recipes = Recipe.query.all()
    recipes = list(map( lambda recipe: recipe.serialize(), recipes))

    for i in range(len(recipes)):
        if(recipes[i]['title']==new_recipe.serialize()['title']):
            raise APIException("found on db" , status_code=400)
            
    print(new_recipe)
    #print(new_user.serialize())
    db.session.add(new_recipe) 
    db.session.commit()
    
    return jsonify({"mensaje": "win :)"}), 201