import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from ..modelos import User 
from flask import Flask, url_for
from datetime import datetime
import json

#Función get para llamar a todos los planetas de la base de datos
@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    planets = list(map( lambda planet: planet.serialize(), planets))  
    return jsonify(planets), 200

#Función get para llamar planetas individualmente de la base de datos
@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    if planet_id==0:
        raise APIException("Id no puede ser igual a 0", status_code=400)  
    planet = Planets.query.get(planet_id)
    if planet == None:
        raise APIException("El planeta no existe", status_code=400)  
    return jsonify(planet.serialize()), 200


#Función post para agregar planetas individuales a la base de datos
@app.route('/planet', methods=['POST'])
def create_new_planet():
    body = request.get_json()
    #validaciones
    if body is None:
        raise APIException("Body está vacío" , status_code=400)
    if body['name'] is None or body['name']=="":
        raise APIException("name es inválido" , status_code=400)

    new_planets = Planets(name=body['name'], diameter=body['diameter'], rotation_Period=body['rotation_Period'], orbital_Period=body['orbital_Period'], gravity=body['gravity'], population=body['population'], climate=body['climate'], terrain=body['terrain'], surface_Water=body['surface_Water'])
    planets = Planets.query.all()
    planets = list(map( lambda planet: planet.serialize(), planets))

    for i in range(len(planets)):
        if(planets[i]['name']==new_planets.serialize()['name']):
            raise APIException("El planeta ya existe" , status_code=400)
            
    print(new_planets)
    #print(new_user.serialize())
    db.session.add(new_planets) 
    db.session.commit()
    
    return jsonify({"mensaje": "Planeta creado exitosamente"}), 201

#Funcion delete para eliminar planetas individuales a la base de datos
@app.route('/planet/<int:item_id>', methods=['DELETE'])
def delete_planet_by_id(item_id):
    if item_id==0:
        raise APIException("Id no puede ser igual a 0", status_code=400)  
    planet = Planets.query.get(item_id)
    if planet == None:
        raise APIException("El planeta no existe", status_code=400)  
    db.session.delete(planet)
    db.session.commit()
    return jsonify("planeta eliminado exitosamente"), 200

