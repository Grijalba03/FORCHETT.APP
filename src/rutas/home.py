import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from ..modelos import home, Categories, Recipe
from flask import Flask, url_for
import json


@app.route('/home', methods=['GET'])
def get_home_data():
    categories = Categories.query.all()
    categories = list(map( lambda category: category.serialize(), categories)) 

    recipes = Recipe.query.all()
    recipes = list(map( lambda recipe: recipe.serialize(), recipes)) 
    dictss = {
        "categories": categories,
        "recepie": recipes
    }

    return jsonify(dictss), 200