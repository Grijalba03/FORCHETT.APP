import os
from flask_admin import Admin
from .db import db

### Importar los modelos #####
from src.modelos import Blocked, User, Recipe, People, Vehicles, Favorite_People, Favorite_Recipes, Favorite_Vehicles 

from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Blocked, db.session))
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Recipe, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Vehicles, db.session))
    admin.add_view(ModelView(Favorite_People, db.session))
    admin.add_view(ModelView(Favorite_Recipes, db.session))
    admin.add_view(ModelView(Favorite_Vehicles, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))