from ..db import db
import os

# Tabla Categories.
class IngredientList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    ingredientsItems = db.Column(db.String(100), nullable=False)
    

#Characters serialize
    def serialize(self):
        return {
            "id": self.id,
            "ingredients": self.ingredientsItems,
            #"ingredientsItems": jsonify(ingredientsItems.serialize()),
            # "ingredientsItems": self.ingredientsItems,
            "recipe_id":Recipe.query.get(self.recipe_id).serialize()['id']
        }
