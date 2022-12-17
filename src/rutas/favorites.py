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
    favorites = list(map(lambda fav: fav.serialize(), favorites)) 
    print("favorites", favorites)
    
     
    return jsonify(favorites), 200


    
                
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


@app.route('/user/favorites', methods=['DELETE'])
def delete_favorite_by_id(item_id):
    if item_id==0:
        raise APIException("Id can't be 0", status_code=400)  
    planet = Planets.query.get(item_id)
    if planet == None:
        raise APIException("El planeta no existe", status_code=400)  
    db.session.delete(planet)
    db.session.commit()
    return jsonify("planeta eliminado exitosamente"), 200