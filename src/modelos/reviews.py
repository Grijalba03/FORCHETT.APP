from ..db import db
import os


# Tabla Pivote: Reviews
 class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #con el nombre de la tabla user y atributo id
    username = db.Column(db.String(15), db.ForeignKey('user.username')) 
    recipes_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))
    recipes_name = db.Column(db.String(150), db.ForeignKey('recipes.name'))
    review = db.Column(db.String(1000), unique=False, nullable=True)
   

     def serialize(self):
        return {
            "id": self.id,
            "username": User.query.get(self.username).serialize()['user.username'],
            "recipes_id": Recipe.query.get(self.recipe_id).serialize()['recipes.id'],
            "recipe_name": Recipe.query.get(self.recipe_name).serialize()['recipes.name'], 
            "review": Review.query.get(self.review).serialize()['reviews.review'] 
        }