import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from .. modelos import Recipe, Favorites
from flask import Flask 
from datetime import datetime
import json  
from ..utils import APIException


@app.route('/user/favorites/<int:user_id>', methods=['GET'])
def get_favorites(user_id):
    if user_id==0:
        raise APIException("ID can't be 0", status_code=400)  
    favorites = Favorites.query.filter_by(user_id = user_id).first()
    print("these are your favorites",favorites) 
    if favorites == None:
        raise APIException("Favorites not found", status_code=400) 
    favorites = favorites.serialize()
    return jsonify(favorites.serialize()), 200
    
                
@app.route('/user/favorites/<int:user_id>', methods=['POST'])
def adding_favorites():
    body = request.get_json()
    if body is None:
        raise APIException("Body está vacío" , status_code=400)
    if body['name'] is None or body['name']=="":
        raise APIException("name es inválido" , status_code=400)

    new_favorite = Favorites(recipe_title=body['recipe_title'], recipe_Id=body['recipe_Id'], username=body['username'], image=body['image'])
    favorites = Favorites.query.all()
    favorites = list(map( lambda item: item.serialize(), favorites))        
    print(new_favorite)
    db.session.add(new_favorite) 
    db.session.commit()
    
    return jsonify({"mensaje": "Favorito agregado exitosamente"}), 201