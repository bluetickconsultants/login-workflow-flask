"""
Module for User model and related functionality.
"""

from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer, BadSignature
from api import db, app

class User(db.Model, UserMixin):
    """
    User model to represent registered users.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    email_confirmation_sent_on = db.Column(db.DateTime, nullable=True)
    email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
    email_confirmed_on = db.Column(db.DateTime, nullable=True)

    def get_reset_token(self, expires_sec=1800):
        """
        Generate a reset token for password reset.
        """
        url_serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"], expires_sec)
        return url_serializer.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        """
        Verify a reset token and return the associated user.
        """
        url_serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
        try:
            user_id = url_serializer.loads(token)['user_id']
        except BadSignature:
            return None
        return User.query.get(user_id)
