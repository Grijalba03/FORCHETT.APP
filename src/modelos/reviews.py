from ..db import db
import os


# Tabla Pivote: Reviews
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=False, nullable=False) #con el nombre de la tabla user y atributo id
    username = db.Column(db.String(15), unique=False, nullable=False)
    recipe_id = db.Column(db.Integer, unique=False, nullable=False)
    recipe_name = db.Column(db.String(150), unique=False, nullable=False)
    review_image = db.Column(db.String(150), unique=False, nullable=True)
    review = db.Column(db.String(1000), unique=False, nullable=True) 
    rating_recipe = db.Column(db.Integer(5), unique=False, nullable=True)
    rating_experience = db.Column(db.Integer(5), unique=False, nullable=True)
   

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "recipe_id": self.recipe_id,
            "recipe_name": self.recipe_name,
            "rating_experience": self.rating_experience, 
            "rating_recipe": self.rating_recipe, 
            "review": self.review, 
            "review_image": self.review_image
        }