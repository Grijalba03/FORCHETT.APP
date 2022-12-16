from ..db import db
import os

# Tabla Categories.
class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(250), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    
    

#Characters serialize
    def serialize(self):

        return {
            "id": self.id,
            "category_name": self.category_name,
            "recipe_id": self.recipe_id,
            # "found": found
        }

