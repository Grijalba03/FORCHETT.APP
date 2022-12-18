from ..db import db
import os


#Table to store: Recipes Images    

class RecipesImages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ruta = db.Column(db.String(300), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
   
def __repr__(self):
    return '<Images %r>' % self.id

    #serialize
def serialize(self):
        return {
            "id": self.id,
            "ruta": self.ruta,
            "user_id": self.user_id
        }