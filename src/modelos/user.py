from ..db import db
import os


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    dietaryPreferences = db.Column(db.String(100), unique=False, nullable=True)
    title =  db.Column(db.String(100), unique=False, nullable=True)
    image =  db.Column(db.String(100), unique=False, nullable=True)
    status =  db.Column(db.Boolean(), unique=False, nullable=True) 
    facebook = db.Column(db.String(100),unique=False, nullable=True)
    twitter = db.Column(db.String(100),unique=False, nullable=True)
    instagram = db.Column(db.String(100),unique=False, nullable=True)
    youtube = db.Column(db.String(100),unique=False, nullable=True)
    # userProfile_id= db.Column(db.Integer, db.ForeignKey('userprofile.id'))
    userProfile = db.relationship("UserProfile", backref="user")
    favorites = db.relationship("Favorites", backref="user")
    recipe = db.relationship("Recipe", backref="user")
    imagen_id = db.relationship("Imagen")



    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "description": self.description,
            "username": self.username, 
            "dietaryPreferences": self.dietaryPreferences,
            "title": self.title,
            "status": self.status,
            "facebook": self.facebook,
            "twitter": self.twitter,
            "instagram": self.instagram,
            "youtube": self.youtube,
            "image": self.image,
            "userProfile": self.userProfile,
            "favorites": self.favorites,
            "imagen_id": self.imagen_id,
            "image_ruta": Imagen.query.get(self.imagen_id).serialize()['ruta']
            #comentario
            # do not serialize the password, its a security breach
        }

