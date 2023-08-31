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
EMAIL_VERIFY_URI = os.getenv("EMAIL_VERIFY_URI")  # Update with your verification URI
REDIRECT_URI = os.getenv("REDIRECT_URI")
