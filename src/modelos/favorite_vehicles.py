
from ..db import db
import os
# from .vehicle import Vehicles 
# from .user import User

# Tabla Pivote: Vehicles/ Favorites
class Favorite_Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #con el nombre de la tabla user y atributo id
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    #Esta es una tabla pivote para relacionar User y Vehicles, relación muchos a muchos

    def serialize(self):
        return {
            "id": self.id,
            "user_email": User.query.get(self.user_id).serialize()['email'],
            "vehicle_name": Vehicles.query.get(self.vehicles_id).serialize()['name']       
        }