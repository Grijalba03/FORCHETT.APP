
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


