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
    favorites = Favorites.query.get(user_id)
    print("these are your favorites",favorites) 

    return jsonify(Favorites), 200

# Favorites = Favorites.query.all()
# Favorites = list(map(lambda favorite: favorite.serialize(), Favorites))
    
                
