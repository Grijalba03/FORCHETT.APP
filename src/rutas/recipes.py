
import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from ..modelos import Recipe 
from flask import Flask, url_for
from datetime import datetime
import json



#Función get para llamar a todas las categorias de la base de datos

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    recipes = list(map( lambda recipe: recipe.serialize(), recipes)) 
    return jsonify(recipes), 200


