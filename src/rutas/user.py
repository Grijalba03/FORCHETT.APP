import os
from ..main import request, jsonify, app, bcrypt, jwt_required, create_access_token, get_jwt_identity, get_jwt
from ..db import db
from ..modelos import User, Blocked
from flask import Flask, url_for
from datetime import datetime, date, time, timezone
import json
from ..utils import APIException
#from flask_jwt_extended import jwt_required


# funcion signup
@app.route('/signup', methods=['POST'])
def signup():
    body = request.get_json()
    # print(body['username'])
    try:
        if body is None:
            raise APIException(
                "Body está vacío o email no viene en el body, es inválido", status_code=400)
        if body['email'] is None or body['email'] == "":
            raise APIException("email es inválido", status_code=400)
        if body['password'] is None or body['password'] == "":
            raise APIException("password es inválido", status_code=400)
        if body['username'] is None or body['username'] == "":
            raise APIException("username es inválido", status_code=400)

        password = bcrypt.generate_password_hash(
            body['password'], 10).decode("utf-8")

        new_user = User(email=body['email'], password=password, username=body['username'],
                        description="", dietaryPreferences="", title="", status=True)
        # users = User.query.all()
        # users = list(map( lambda user: user.serialize(), users))

        # for i in range(len(users)):
        #     if(users[i]['email']==new_user.serialize()['email']):
        #         raise APIException("El usuario ya existe" , status_code=400)

        user = User.query.filter_by(username=body['username'])#.first()
        if not user: 
             raise APIException("User already exists" , status_code=400)
        print(new_user)
        # print(new_user.serialize())
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"response": "User successfully created"}), 201

    except Exception as err:
        db.session.rollback()
        print(err)
        return jsonify({"response": "error registering user"}), 500


# funcion login
@app.route('/login', methods=['POST'])
def user_login():
    body = request.get_json()
    # email = body['email']
    username = body['username']
    pw = body['password']  # campo tabla usuario
    # entontrar la primera coincidencia
    user = User.query.filter_by(username=username).first()
    # user = User.query.filter_by(email=email).first()
    print('username', username)
    if username is None:
        # documentar errores con codigo (recomendacion)
        raise APIException("Inválido, intenta de nuevo1", status_code=400)
    # comparando passwords, si no coinciden levantamos el API exception
    if not bcrypt.check_password_hash(user.password, pw):
        raise APIException("Inválido, intenta de nuevo2", status_code=400)
    # crear token para autenticación
    token = create_access_token(identity=user.id)
    return jsonify({"token": token})

# funcion logout


@app.route('/logout', methods=['POST'])  # cualquier metodo vale
@jwt_required()  # añadiendo proteccion con token
def user_logout():
    jti = get_jwt()['jti']  # jason token identifier
    # haciendo query del token segun el jti
    foundtoken = Blocked.query.filter_by(blocked_token=jti).first()
    if not foundtoken is None:
        raise APIException("Token inválido, o ya expiró", status_code=400)
    created = datetime.now(timezone.utc)  # zona horaria del usuario
    print(created)
    identidad = get_jwt_identity()  # almacenando el ID del usuario
    user = User.query.get(identidad)
    email = user.email
    new_blocked = Blocked(blocked_token=jti, email=email, created=created)
    db.session.add(new_blocked)
    db.session.commit()
    return jsonify({"Mensaje": "Sesión cerrada exitosamente!"})


#funcion profile con proteccion
@app.route('/vip', methods=['POST'])#cualquier metodo vale
@jwt_required() #añadiendo proteccion con token
def user_vip():
    identidad = get_jwt_identity() #almacenando el ID del usuario 
    jti = get_jwt()['jti']  #revisar status del token
    foundtoken = Blocked.query.filter_by(blocked_token=jti).first() #haciendo query del token segun el jti

    if not foundtoken is None:
        raise APIException("Token inválido, o ya expiró", status_code=400)
    user = User.query.get(identidad)
    return jsonify({"Usuario": user.email})


# Función get para llamar a todos los usuarios de la base de datos
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    # print(users)
    users = list(map(lambda user: user.serialize(), users))
    # print(users)
    return jsonify(users), 200

# funcion para traer usuarions con ID


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    if user_id == 0:
        raise APIException("Id no puede ser igual a 0", status_code=400)
    user = User.query.get(user_id)
    if user == None:
        raise APIException("El usuario no existe", status_code=400)
    # print(user.serialize())
    return jsonify(user.serialize()), 200

# funcion para eliminar usuarions con ID


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    if user_id == 0:
        raise APIException("Id no puede ser igual a 0", status_code=400)
    user = User.query.get(user_id)
    if user == None:
        raise APIException("El usuario no existe", status_code=400)
    # print(user.serialize())
    db.session.delete(user)
    db.session.commit()
    return jsonify("usuario eliminado exitosamente"), 200


@app.route('/helloprotected', methods=['get'])  # endpoint
@jwt_required()  # decorador que protege al endpoint
def hello_protected():  # definición de la función
    #claims = get_jwt()
    # imprimiendo la identidad del usuario que es el id
    print("id del usuario:", get_jwt_identity())
    # búsqueda del id del usuario en la BD
    user = User.query.get(get_jwt_identity())

    # get_jwt() regresa un diccionario, y una propiedad importante es jti
    jti = get_jwt()["jti"]

    #tokenBlocked = TokenBlockedList.query.filter_by(token=jti).first()
    # cuando hay coincidencia tokenBloked es instancia de la clase TokenBlockedList
    # cuando No hay coincidencia tokenBlocked = None

    # if isinstance(tokenBlocked, TokenBlockedList):
    #    return jsonify(msg="Acceso Denegado")

    response_body = {
        "message": "token válido",
        "user_id": user.id,  # get_jwt_identity(),
        "user_email": user.email
    }

    return jsonify(response_body), 200


@app.route('/lista-usuarios', methods=['get'])
@jwt_required()
def allUsers():
    users = User.query.all()  # Objeto de SQLAlchemy
    users = list(map(lambda item: item.serialize(), users))

    response_body = {
        "lista": users
    }
    return jsonify(response_body), 200




@app.route('/account/<string:username>', methods=['PUT'])
@jwt_required() 
def update_user_account(username):
    identidad = get_jwt_identity()
    jti = get_jwt()['jti']
    foundtoken = Blocked.query.filter_by(blocked_token=jti).first()

    if not foundtoken is None:
        raise APIException("Token inválido, o ya expiró", status_code=400)
    user = User.query.get(identidad)

    body = request.get_json()
    if body is None:
        raise APIException("Error: body is empty", status_code=400)
    
    if body['title'] != "":
        title = body['title']
        facebook =  body['facebook']
        twitter =  body['twitter']
        instagram =  body['instagram']
        youtube =  body['youtube']
        dietaryPreferences =  body['dietaryPreferences']
        # print(userTitle)


    user.title = title
    user.facebook = facebook
    user.twitter = twitter
    user.instagram = instagram
    user.youtube = youtube
    user.dietaryPreferences = dietaryPreferences

    db.session.commit()
    return jsonify({"Result": "updated"})


# Usser Account -> Change password
@app.route('/account/password/<string:username>', methods=['PUT'])
@jwt_required() 
def update_user_account_password(username):
    userId = get_jwt_identity()
    jti = get_jwt()['jti']
    foundtoken = Blocked.query.filter_by(blocked_token=jti).first()

    if not foundtoken is None:
        raise APIException("Token has already expired or invalid.", status_code=400)
    user = User.query.get(userId)
    body = request.get_json()

    try:
        if body is None:
            raise APIException("Error: body is empty", status_code=400)
        if body['current-password'] is None or body['current-password'] == "":
            raise APIException("Current password field cannot be empty.", status_code=400)
        print("current pass: ", body['current-password'])
        if body['new-password'] is None or body['new-password'] == "":
            raise APIException("New password field cannot be empty.", status_code=400)
        print("new pass: ", body['new-password'])
        if body['confirm-password'] is None or body['confirm-password'] == "":
            raise APIException("Confirm password field cannot be empty.", status_code=400)
        print("confirm pass: ", body['confirm-password'])
        if str(body['new-password']) != str(body['confirm-password']) :
            raise APIException('New Password and Confirm password should be the same.', status_code=400)

        print('body', body)
        genNewPassword = bcrypt.generate_password_hash(
            body['new-password'], 10).decode("utf-8")
        newPass = User(password=genNewPassword)
        print("genNew ", genNewPassword)
        user = User.query.get(get_jwt_identity())
        user.password = genNewPassword
        print("pass ", user)
        db.session.commit()
        return jsonify({"Result": "Password updated."})
    
    except Exception as err:
        db.session.rollback()
        print(err)
        return jsonify({"response": "error updating user password"}), 500
    