"""
config.py

This module contains the configuration settings for your Flask application.
"""
import os

SECRET_KEY = os.urandom(20)
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
DATABASE_URL = "mysql://root:root@localhost/mysql_python"
EMAIL_PASS = "dvwavvpnznkqqcvv"
EMAIL_USER = "cloudbluetick@gmail.com"
EMAIL_VERIFY_URI = "http://127.0.0.1:5000"  # Update with your verification URI
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = "aamirbaugwala@gmail.com"
MAIL_PASSWORD = "aamir123"
