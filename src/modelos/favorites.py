from ..db import db
import os
from .recipe import Recipe




# Pivot Table: Recipe/ Favorites    

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #we use the table name: user and ID attribute
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #we use the table name: user and ID attribute
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
   
   

    #serialize
    def serialize(self):
        return {
            "id": self.id,
            "recipe_title":Recipe.query.get(self.recipe_title).serialize()['title'],
            "recipe_id":Recipe.query.get(self.recipe_id).serialize()['id'] 
            
        }