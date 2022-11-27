from ..db import db


class userProfile (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
   
    


def serialize(self): 
        return { 
            "id": self.id, 
            "username":self.username, 
            "user_id": User.query.get(self.user_id).serialize()['id'],
            "Image":User.query.get(self.user_id).serialize()['Image'],
            "Facebook":User.query.get(self.user_id).serialize()['Facebook'],
            "Twitter":User.query.get(self.user_id).serialize()['Twitter'],
            "Instagram":User.query.get(self.user_id).serialize()['Instagram'],
            "Youtube":User.query.get(self.user_id).serialize()['Youtube'], 
            "Title":User.query.get(self.user_id).serialize()['Title'],
            "dietaryPreferences":User.query.get(self.serialize)['dietaryPreferences']
        }

        
     

