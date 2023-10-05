"""
config.py

This module contains the configuration settings for your Flask application.
"""
import os

SECRET_KEY = os.urandom(20)
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
DATABASE_URL = "mysql://root:root@localhost/mysql_python"
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_USER = os.getenv("EMAIL_USER")
# Update with your verification URI
EMAIL_VERIFY_URI = os.getenv("EMAIL_VERIFY_URI")
REDIRECT_URI = os.getenv("REDIRECT_URI")
GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
FRONTEND_URL = os.getenv('FRONTEND_URL')
