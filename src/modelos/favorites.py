from ..db import db
import os


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #we use the table name: user and ID attribute
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #we use the table name: user and ID attribute
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('recipe.category'))
   