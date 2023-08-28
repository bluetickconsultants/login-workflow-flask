from app.authentication import login,register
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from config import SECRET_KEY
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)

SECRET_KEY = app.config['SECRET_KEY'] 
SQLALCHEMY_DATABASE_URI = app.config['SQLALCHEMY_DATABASE_URI'] 


db = SQLAlchemy(app)
mail = Mail(app)
bcrypt = Bcrypt(app)
s = URLSafeTimedSerializer(app.config["SECRET_KEY"])



