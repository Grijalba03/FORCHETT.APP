from ..db import db
import os


class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categories_list = db.Column(db.Integer, db.ForeignKey('categories.id'))
    recipe_list = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    #serialize
    def serialize(self):
        return {
            "id": self.id,
            "categories_title": Categories.query.get(self.categories_list).serialize()['category_name'],
            "all_recipe" : Recipe.query.get(self.recipe_list).serialize()['title']
        }