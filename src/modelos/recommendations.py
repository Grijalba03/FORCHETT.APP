
from ..db import db
import os

# Tabla Pivote: Recommendations/ Favorites
class Recommendations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #con el nombre de la tabla user y atributo id
    username = db.Column(db.String(15), db.ForeignKey('user.username')) 
    recipes_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    recipes_name = db.Column(db.String(150), db.ForeignKey('recipes.name'))

    def serialize(self):
        return {
            "id": self.id,
            "user_email": User.query.get(self.user_id).serialize()['email'],
            "username": User.query.get(self.username).serialize()['username'],       
            "recipes_id": Recipe.query.get(self.recipes_id).serialize()['recipe.id']       
            "recipes_name": Recipe.query.get(self.recipes_name).serialize()['recipe.name']       
        }