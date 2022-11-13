from ..db import db
import os
from .favorite_recipes import Favorite_Recipes


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=True)
    username = db.Column(db.String(15), unique=False, nullable=False)
    dietaryPreferences = db.Column(db.String(100), unique=False, nullable=True)
    userTitle =  db.Column(db.String(100), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "description": self.description,
            "username": self.username, 
            "dietaryPreferences": self.dietaryPreferences,
            "userTitle": self.userTitle
            # do not serialize the password, its a security breach
        }

