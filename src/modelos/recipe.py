from ..db import db
import os
from .favorite_recipes import Favorite_Recipes

# Tabla Recipe
class Recipe (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    favorite_recipes = db.relationship("Favorite_Recipes", backref="recipe")
    status =  db.Column(db.Boolean(), unique=False, nullable=True)
    category = db.Column(db.Integer, unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=True)
    title =  db.Column(db.String(250), nullable=False)
    servings = db.Column(db.String(250), nullable=False)
    prep = db.Column(db.String(250), nullable=False)
    bake = db.Column(db.String(250), nullable=False)
    protein =  db.Column(db.String(250), nullable=True)
    carbs =  db.Column(db.String(250), nullable=True)
    fat =  db.Column(db.String(250), nullable=True)
    preparation = db.Column(db.String(250), nullable=False)
    ingredients =  db.Column(db.String(500), nullable=False)
    free_of =  db.Column(db.String(500), nullable=True)
    image = db.Column(db.String(300), nullable=True)
    description = db.Column(db.String(300), nullable=False)



    #Recipe serialize
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "favorite_recipes":self.favorite_recipes,
            "status": self.status,
            "category": self.category,
            "rating": self.rating,
            "title": self.title,
            "servings": self.servings,
            "prep": self.prep,
            "bake": self.bake,
            "protein": self.protein,
            "carbs": self.carbs,
            "fat": self.fat,
            "preparation": self.preparation,
            "ingredients": self.ingredients,
            "free_of": self.free_of,
            "image": self.image,
            "description": self.description

        }

