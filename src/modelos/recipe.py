from ..db import db
import os

# Tabla Recipe
class Recipe (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
   recipe_favorite = db.relationship("Favorite_Recipe", backref="recipe")

    #Recipe serialize
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_Period": self.rotation_Period,
            "orbital_Period": self.orbital_Period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_Water": self.surface_Water
        }

