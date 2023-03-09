from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# create the Flask app
app = Flask(__name__)

# set the app config
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASS']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the database object
db = SQLAlchemy(app)

# import the routes module
from app import routes
