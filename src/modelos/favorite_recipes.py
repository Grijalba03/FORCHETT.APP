from ..db import db
import os
# from .planet import Planets
from .user import User

# Tabla Pivote: Recipe/ Favorites    

class Favorite_Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #con el nombre de la tabla user y atributo id
    username = db.Column(db.String(15), db.ForeignKey('user.username')) 
    recipes_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))

    #serialize
    def serialize(self):
        return {
            "id": self.id,
            "username": User.query.get(self.username).serialize()['username'],
            "recipe_name": Recipe.query.get(self.recipe_id).serialize()['recipename'] 
            
        }