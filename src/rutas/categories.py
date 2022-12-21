
import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from ..modelos import Categories, Recipe
from flask import Flask, url_for
from datetime import datetime
import json
from ..utils import APIException




#GET function to call all categories from the DB

@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Categories.query.all()
    categories = list(map( lambda category: category.serialize(), categories)) 
    return jsonify(categories), 200

#Función get para llamar categorías individualmente de la base de datos
@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category_by_id(category_id):
    if category_id==0:
        raise APIException("ID can't be 0", status_code=400)  
    category = Categories.query.get(category_id)
    if category == None:
        raise APIException("Category not found", status_code=400)  
    category = category.serialize()
    auxiliar = Recipe.query.filter(Recipe.category==category_id).all()
    auxiliar = list(map(lambda item: item.serialize(), auxiliar))
    category['found'] = auxiliar
    print('entramos al endpoint categorias')
    print(auxiliar)
    return jsonify(category), 200

#Post function to add a new category to the DB 
@app.route('/category', methods = ['POST'])
def create_new_category():
    body = request.get_json()
    if body is None:
        raise APIException("Body is empty", status_code=400)
    if body ['category_name'] is None or body['category_name'] =="":
        raise APIException("Name is invalid", status_code=400) 

    new_category = category(category_name=body['category_name'])
    category = Categories.query.all() 
    category = list(map(lambda categories: categories.serialize(), category))  

    db.session.add(new_category)   
    db.session.commit   
         