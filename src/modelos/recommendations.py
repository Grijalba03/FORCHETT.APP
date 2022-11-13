
from ..db import db
import os

# Tabla Pivote: Recommendations/ Favorites
class Recommendations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False) #con el nombre de la tabla user y atributo id
    username = db.Column(db.String(15), unique=False, nullable=False)
    recipe_id =  db.Column(db.Integer, unique=False, nullable=False)
    recipe_name =  db.Column(db.String(100), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,  
            "recipe_id": self.recipe.id,      
            "recipe_name": self.recipe.name      
        }