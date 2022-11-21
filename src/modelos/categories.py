from ..db import db
import os


# Tabla Categories.
class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drinks = db.Column(db.String(100), nullable=False)
    breakfast  = db.Column(db.String(250))
    brunch  = db.Column(db.String(250))
    lunch  = db.Column(db.String(250))
    dinner  = db.Column(db.String(250))
    salads = db.Column(db.String(250))
    kids = db.Column(db.String(250))
    snacks = db.Column(db.String(250))
    vegetarian = db.Column(db.String(250))
    vegan = db.Column(db.String(250))
    

#Characters serialize
    def serialize(self):
        return {
            "id": self.id,
            "drinks": self.drinks,
            "breakfast": self.breakfast,
            "brunch": self.brunch,
            "lunch": self.lunch,
            "dinner": self.dinner,
            "salads": self.salads,
            "kids": self.kids,
            "snacks": self.snacks,
            "vegetarian": self.vegetarian,
            "vegan": self.vegan
        }

