from ..db import db
import os
from .recipe import Recipe
from .user import User




# Pivot Table: Recipe/ Images    

class RecipesImages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #we use the table name: user and ID attribute
    image_id = db.Column(db.Integer, db.ForeignKey('imagen.id')) #we use the table name: user and ID attribute
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
   
   
   

    #serialize
    def serialize(self):
        return {
            "id": self.id,
            "recipe_id":Recipe.query.get(self.recipe_id).serialize()['id'], 
            "recipe_title":Recipe.query.get(self.recipe_id).serialize()['title'],
            "recipe_image":Imagen.query.get(self.imagen_id).serialize()['ruta'],
            "image_id":Imagen.query.get(self.imagen_id).serialize()['id']     
            
        }