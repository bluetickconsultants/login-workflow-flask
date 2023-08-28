"""
api/__init__.py

This module initializes the Flask application and sets up various components and configurations.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
from api.authentication import login, register
from config import SECRET_KEY

app = Flask(__name__)

SECRET_KEY = app.config['SECRET_KEY']
SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy(app)
mail = Mail(app)
bcrypt = Bcrypt(app)
s = URLSafeTimedSerializer(app.config["SECRET_KEY"])
