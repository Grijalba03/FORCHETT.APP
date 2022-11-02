from ..db import db
import os

# Tabla Characters
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    height = db.Column(db.Float)
    mass = db.Column(db.Float)
    hair_color  = db.Column(db.String(250))
    skin_color  = db.Column(db.String(250))
    eye_color  = db.Column(db.String(250))
    birth_year = db.Column(db.Integer)
    gender = db.Column(db.String(250))
    homeworld = db.Column(db.String(250))
    people_favorite = db.relationship("Favorite_People", backref="people")

#Characters serialize
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld
        }

# Tabla Pivote: Characters/ Favorites
class Favorite_People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #con el nombre de la tabla user y atributo id
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    #Esta es una tabla pivote para relacionar User y Characters, relación muchos a muchos

    def serialize(self):
        return {
            "id": self.id,
            "user_email": User.query.get(self.user_id).serialize()['email'],
            "character_name": People.query.get(self.people_id).serialize()['name']          
        }