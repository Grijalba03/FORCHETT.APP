from ..db import db
import os


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(120), unique=True, nullable=False)
    lastName = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=True)
    username = db.Column(db.String(15), unique=False, nullable=False)
    dietaryPreferences = db.Column(db.String(100), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastName": self.lastName,
            "email": self.email,
            "description": self.description,
            "username": self.username, 
            "dietaryPreferences": self.dietaryPreferences
            # do not serialize the password, its a security breach
        }

