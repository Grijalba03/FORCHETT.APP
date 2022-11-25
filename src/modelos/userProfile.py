from ..db import db


class userProfile (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
   
    


def serialize(self): 
        return { 
            "id": self.id, 
            "username":self.username, 
            "user_id": User.query.get(self.user_id).serialize()['id'],
            "userImage":User.query.get(self.user_id).serialize()['userImage'],
            "userFacebook":User.query.get(self.user_id).serialize()['userFacebook'],
            "userTwitter":User.query.get(self.user_id).serialize()['userTwitter'],
            "usreInstagram":User.query.get(self.user_id).serialize()['userInstagram'],
            "userYoutube":User.query.get(self.user_id).serialize()['userYoutube'], 
            "userTitle":User.query.get(self.user_id).serialize()['userTitle'],
            "dietaryPreferences":User.query.get(self.serialize)['dietaryPreferences']
        }

        
     

