from ..db import db
import os
from .recipe import Recipe
from .user import User




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
            "recipe_title":Recipe.query.filter_by(recipe_title = recipe_title).first(),
            "recipe_id":Recipe.query.get(self.recipe_id).serialize()['id'], 
            "username": User.query.filter_by(user_username = user_username).serialize()['username'],
            "image": User.query.filter_by(user_image = user_image).serialize()['image'],
             
            
        }