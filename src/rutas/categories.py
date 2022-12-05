
import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from ..modelos import Categories 
from flask import Flask, url_for
from datetime import datetime
import json



#GET functin to call all categories from the DB

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
    return jsonify(category.serialize()), 200
