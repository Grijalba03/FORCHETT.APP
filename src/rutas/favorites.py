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
    favorites = Favorites.query.filter_by(user_id = user_id).all()
    print("these are your favorites",favorites) 
    if favorites == None:
        raise APIException("Favorites not found", status_code=400) 
    # favorites = favorites.serialize()
    favorites = list(map( lambda fav: fav.serialize(), favorites)) 
    return jsonify(favorites), 200
    
                
@app.route('/user/favorites/<int:user_id>', methods=['POST'])
def adding_favorites(user_id):
    body = request.get_json()
    if body is None:
        raise APIException("id está vacío" , status_code=400)
    # if body['id'] is None or body['id']=="":
    #     raise APIException("id es inválido" , status_code=400)

    new_favorite = Favorites(user_id=body['user_id'], recipe_id=body['recipe_id'])
    # favorites = Favorites.query.filter_by(user_id)
    # favorites = list(map( lambda item: item.serialize(), favorites))        
    print(new_favorite)
    db.session.add(new_favorite) 
    db.session.commit()
    
    return jsonify({"mensaje": "Favorito agregado exitosamente"}), 201