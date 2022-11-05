from ..db import db
import os

#Tokens bloqueados
class Blocked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blocked_token = db.Column(db.String(250))
    email = db.Column(db.String(250), unique=True, nullable=False)
    created = db.Column(db.DateTime)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "blocked token": self.blocked_token,
            "created": self.DateTime
        }