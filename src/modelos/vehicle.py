from ..db import db
import os

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(250))
    vehicle_class = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Float)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Float)
    cargo_capacity = db.Column(db.Float)
    consumables = db.Column(db.String(250))
    vehicles_favorite = db.relationship("Favorite_Vehicles", backref="vehicles")

    #serialize
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables
        }
