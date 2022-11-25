from ..db import db
import os
from .favorite_recipes import Favorite_Recipes
from .userProfile import userProfile


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    dietaryPreferences = db.Column(db.String(100), unique=False, nullable=True)
    userTitle =  db.Column(db.String(100), unique=False, nullable=True)
    userstatus =  db.Column(db.Boolean(), unique=False, nullable=True) 
    userFacebook = db.Column(db.String(100),unique=False, nullable=True)
    userTwitter = db.Column(db.String(100),unique=False, nullable=True)
    userInstagram = db.Column(db.String(100),unique=False, nullable=True)
    userYoutube = db.Column(db.String(100),unique=False, nullable=True)
    userImage = db.Column(db.String(100),unique=False, nullable=True)
    userRecipe = db.Column(db.String(1000),unique=False, nullable=True)
    # userProfile_id= db.Column(db.Integer, db.ForeignKey('userprofile.id'))
    userProfile = db.relationship("userProfile", backref="user")



    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "description": self.description,
            "username": self.username, 
            "dietaryPreferences": self.dietaryPreferences,
            "userTitle": self.userTitle,
            "userStatus": self.userstatus,
            "userFacebook": self.userFacebook,
            "userTwitter": self.userTwitter,
            "userInstagram": self.userInstagram,
            "userYoutube": self.userYoutube,
            "userImage": self.userImage,
            "userProfile": self.userProfile
            #comentario
            # do not serialize the password, its a security breach
        }

