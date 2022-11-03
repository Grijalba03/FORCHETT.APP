from ..db import db
import os
# from .planet import Planets
# from .user import User

# Tabla Pivote: Planets/ Favorites    
#Esta es una tabla pivote para relacionar User y Planets, relación muchos a muchos
class Favorite_Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #con el nombre de la tabla user y atributo id
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))

    #serialize
    def serialize(self):
        return {
            "id": self.id,
            "user_email": User.query.get(self.user_id).serialize()['email'],
            "planet_name": Planets.query.get(self.planet_id).serialize()['name'],
        }