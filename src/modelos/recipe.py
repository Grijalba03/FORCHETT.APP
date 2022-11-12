from ..db import db
import os
from .favorite_recipes import Favorite_Recipes

# Tabla Recipe
class Recipe (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    favorite_recipes = db.relationship("Favorite_Recipes", backref="recipe")

    #Recipe serialize
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            
        }

