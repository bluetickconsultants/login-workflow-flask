"""
Module for User registration, confirmation, and related functionality.
"""

import datetime
from flask import jsonify, render_template_string, request,Blueprint
from api.authentication.models import User,db
from api import  mail, bcrypt, s, app
from flask_mail import Message
from utils.login_utils import create_verification_email_body, email_verified_success_html

# Constants
EMAIL_USER = app.config['MAIL_USERNAME']
EMAIL_PASS = app.config['MAIL_PASSWORD']
EMAIL_VERIFY_URI = app.config['EMAIL_VERIFY_URI']


register_routes = Blueprint('register', __name__)

@register_routes.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    """
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        email = data.get('email')
        password = data.get('password')

        # Check if email and password are provided in the request body
        if not email or not password:
            return jsonify({'error': 'Email and password are required.'}), 400
        existing_user_email = User.query.filter_by(email=email).first()
        if existing_user_email:
            return jsonify({'error': 'Email already exists.'}), 401
        else:
            try:
                password_encoded = password.encode('utf-8')
                hashed_password = bcrypt.generate_password_hash(password_encoded)
                new_user = User(email=email, password=hashed_password)
                
                db.session.add(new_user)
                db.session.commit()
                
                token = s.dumps(email, salt='email-confirmation-link')
                confirm_route = 'confirm'
                link = f'{EMAIL_VERIFY_URI}/{confirm_route}/{token}'

                html_content = create_verification_email_body(link)
                
                msg = Message('verification', sender=EMAIL_USER, recipients=[email], html=html_content)
                
                mail.send(msg) 
                
                return jsonify({"message": "User created successfully"}), 200
            except Exception as exception:
                db.session.rollback()
                return jsonify({'error': str(exception)}), 401

@register_routes.route('/confirm/<token>')
def confirm(token):
    """
    Confirm user's email address.
    """
    try:
        email = s.loads(token, salt='email-confirmation-link', max_age=1800)
        user = User.query.filter_by(email=email).first()
        if user:
            user.email_confirmed = True
            user.email_confirmed_on = datetime.datetime.now()
            db.session.commit()
            
            login_url = "http://pdf.bluetickconsultants.com/login.html"
            html_content = email_verified_success_html(login_url)
            
            return render_template_string(html_content)
        else:
            return "User not found."
    except Exception:
        return "Link expired or invalid."
    
app.register_blueprint(register_routes)
