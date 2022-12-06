from ..db import db
from .user import User


class UserProfile (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
   
    


    def serialize(self): 
        user = User.query.get(self.user_id).serialize()

        return { 
            "id": self.id, 
           
            "username":self.username, 
            "user_id": User.query.get(self.user_id).serialize()['id'],
            "image":user['image'],
            "facebook":user['facebook'],
            "twitter":user['twitter'],
            "instagram":user['instagram'],
            "youtube":user['youtube'], 
            "title":user['title'],
            "dietaryPreferences":user['dietaryPreferences']
        }
     

