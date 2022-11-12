from ..db import db
import os




# Tabla Pivote: Recipe/ Favorites    

class Favorite_Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #con el nombre de la tabla user y atributo id
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
   

    #serialize
    def serialize(self):
        return {
            "id": self.id,
            "username": User.query.get(self.user_id).serialize()['username'],
            "recipe_name": Recipe.query.get(self.recipe_id).serialize()['name'],
            "recipe_id": Recipe.query.get(self.recipe_id).serialize()['id'] 
            
        }