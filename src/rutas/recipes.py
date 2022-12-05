
import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from ..modelos import Recipe 
from flask import Flask, url_for
from datetime import datetime
import json



#Función get para llamar a todas las recetas de la base de datos

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    recipes = list(map( lambda recipe: recipe.serialize(), recipes)) 
    return jsonify(recipes), 200


#Función get para llamar recetas individualmente de la base de datos
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe_by_id(recipe_id):
    if recipe_id==0:
        raise APIException("Id can't be 0", status_code=400)  
    recipe = Recipe.query.get(recipe_id)
    if recipe == None:
        raise APIException("Recipe not found", status_code=400)  
    return jsonify(recipe.serialize()), 200