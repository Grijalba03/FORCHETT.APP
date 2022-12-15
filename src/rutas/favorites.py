import os
from ..main import request, jsonify, app, bcrypt, jwt_required, get_jwt, get_jwt_identity
from ..db import db
from .. modelos import Recipe, Favorites
from flask import Flask 
from datetime import datetime
import json  
from ..utils import APIException


@app.route('/user/favorites', methods=['GET'])
@jwt_required()
def get_favorites():
    user_id = get_jwt_identity() #almacenando el ID del usuario 
    if user_id==0:
        raise APIException("ID can't be 0", status_code=400)  
    favorites = Favorites.query.filter_by(user_id = user_id).all()
    print("these are your favorites",favorites) 
    if favorites == None:
        raise APIException("Favorites not found", status_code=400) 
    favorites = list(map(lambda fav: fav, favorites)) 
    # print("favorites", favorites)
    
    str = json.dumps(favorites)
    print(str)
    return jsonify(str), 200
    
                
@app.route('/user/favorites', methods=['POST'])
@jwt_required()
def adding_favorites():
    body = request.get_json()
    user_id = get_jwt_identity()
    if body is None:
        raise APIException("id está vacío" , status_code=400)
    if body['recipe_id'] is None or body['recipe_id']=="":
       raise APIException("id es inválido" , status_code=400)

    new_favorite = Favorites(user_id= user_id, recipe_id=body['recipe_id'])      
    db.session.add(new_favorite) 
    db.session.commit()
    
    return jsonify({"mensaje": "Favorito agregado exitosamente"}), 201