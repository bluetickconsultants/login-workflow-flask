from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
from flask_sqlalchemy import SQLAlchemy
from config import SECRET_KEY


app = Flask(__name__)

mail = Mail(app)
bcrypt = Bcrypt(app)
s = URLSafeTimedSerializer(SECRET_KEY)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)