from flask import Flask
# import log forms from the form file
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# function to fetch all info from the vehicle database
# vehicles = classes.vehicles.vehiclesDB.queryVehiclesGeneral()
app = Flask(__name__)
app.app_context().push() # gives the context to create the db from outside the application
app.config['SECRET_KEY'] = '3a91a34e53b72ed106d2bd8e87fe37ae' # secret key for the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workersAndVehicles.db'
db = SQLAlchemy(app) # Creates the database instance. We can represent the db structures as classes or models
bcrypt = Bcrypt(app)
login_manager = LoginManager(app) # adding the log in feature
register_user_code = 'e3b0c44298'

from serverFlask import routes

