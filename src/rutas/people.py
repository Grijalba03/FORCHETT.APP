
import os
from ..main import request, jsonify, app, bcrypt
from ..db import db
from ..modelos import User
from flask import Flask, url_for
from datetime import datetime
import json

#Función get para llamar a todos los personajes de la base de datos
@app.route('/people', methods=['GET'])
def get_people():
    peoples = People.query.all()
    #print(users)
    peoples = list(map( lambda people: people.serialize(), peoples)) 
    #print(users)  
    return jsonify(peoples), 200

#Función get para llamar personajes individualmente de la base de datos
@app.route('/people/<int:people_id>', methods=['GET'])
def get_people_by_id(people_id):
    if people_id==0:
        raise APIException("Id no puede ser igual a 0", status_code=400)  
    person = People.query.get(people_id)
    if person == None:
        raise APIException("El usuario no existe", status_code=400)  
    return jsonify(person.serialize()), 200

#Función post para agregar personajes individuales a la base de datos
@app.route('/people', methods=['POST'])
def create_new_person():
    body = request.get_json()
    #validaciones
    if body is None:
        raise APIException("Body está vacío" , status_code=400)
    if body['name'] is None or body['name']=="":
        raise APIException("name es inválido" , status_code=400)

    new_character = People(name=body['name'], height=body['height'], mass=body['mass'], hair_color=body['hair_color'], skin_color=body['skin_color'], eye_color=body['eye_color'], birth_year=body['birth_year'], gender=body['gender'], homeworld=body['homeworld'])
    characters = People.query.all()
    characters = list(map( lambda character: character.serialize(), characters))

    # for i in range(len(characters)):
    #     if(characters[i]['name']==new_character.serialize()['name']):
    #         raise APIException("El personaje ya existe" , status_code=400)
            
    print(new_character)
    #print(new_user.serialize())
    db.session.add(new_character) 
    db.session.commit()
    
    return jsonify({"mensaje": "Personaje creado exitosamente"}), 201

#Función get para actualizar personajes individualmente de la base de datos
@app.route('/people/<int:people_id>', methods=['PUT'])
def put_people_by_id(people_id):
    if people_id==0:
        raise APIException("Id no puede ser igual a 0", status_code=400)  
    person = People.query.get(people_id)#buscar por ID es la manera mas eficiente de realizar busquedas en las bases de datos
    if person == None:
        raise APIException("El usuario no existe", status_code=400) 
    body = request.get_json()
    #validaciones
    if body is None:
        raise APIException("Body está vacío" , status_code=400)
    #validamos si viene el campo name en el body o no (despues de hacer el request.get_json())
    if not body['name'] is None:
        person.name = body['name']
    db.session.commit()     
    return jsonify(person.serialize()), 200

#Función post para realizar busqueda de personajes en la base de datos
@app.route('/people/busqueda', methods=['POST'])
def busqueda_people():
    body = request.get_json()
    #validaciones
    if body is None:
        raise APIException("Body está vacío" , status_code=400)
    if not body['name'] is None:    
        found = People.query.filter(People.name==body['name']).all() #va a encontrar todas las coincidencias        
        found = list(map( lambda item: item.serialize(), found))
        print(found)
    if found == None:
        raise APIException("El personaje no existe", status_code=400)  
    return jsonify(found), 200

#Funcion delete para eliminar personajes individuales a la base de datos
@app.route('/people/<int:item_id>', methods=['DELETE'])
def delete_character_by_id(item_id):
    if item_id==0:
        raise APIException("Id no puede ser igual a 0", status_code=400)  
    character = People.query.get(item_id)
    if character == None:
        raise APIException("El personaje no existe", status_code=400)  
    db.session.delete(character)
    db.session.commit()
    return jsonify("personaje eliminado exitosamente"), 200