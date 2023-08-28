"""
run.py

This module is used to run your Flask application.
"""
from app import app


if __name__ == '__main__':
    app.run(debug=True)
