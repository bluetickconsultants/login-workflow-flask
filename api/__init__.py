"""
api/__init__.py

This module initializes the Flask application and sets up various components and configurations.
"""
from flask import Flask

from flask_bcrypt import Bcrypt
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer

from config import SECRET_KEY,SQLALCHEMY_DATABASE_URI



app = Flask(__name__)



app.config['SECRET_KEY']= SECRET_KEY 
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI 


mail = Mail(app)
bcrypt = Bcrypt(app)
s = URLSafeTimedSerializer(app.config["SECRET_KEY"])



