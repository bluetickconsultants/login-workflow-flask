"""
Module for user authentication login routes.
"""

import jwt
import datetime
from flask import jsonify, render_template_string, request
from app.authentication.models import User
from app import db, mail, bcrypt, s, app
from flask_mail import Message
from utils.login_utils import (
    create_reset_password_body,
    password_reset_form_html,
    password_reset_success_html,
)

EMAIL_USER = app.config['MAIL_USERNAME']
EMAIL_PASS = app.config['MAIL_PASSWORD']
EMAIL_VERIFY_URI = app.config['EMAIL_VERIFY_URI']



@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate user login.
    """
    data = request.get_json()
    print("Login Request Data:", data)

    # Check if email and password are provided in the request body
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'error': 'Email and password are required.'}), 400

    # Check if the user exists
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'Invalid credentials.'}), 400

    # Check if the user's email is confirmed
    if not user.email_confirmed:
        return jsonify({'error': 'Please confirm your email before logging in.'}), 401

    # Check if the password matches
    if not bcrypt.check_password_hash(user.password, password.encode('utf-8')):
        return jsonify({'error': 'Invalid credentials. Incorrect password.'}), 401

    # If the credentials are valid, create a JWT token
    token_payload = {
        'email': email,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # Set session timeout to 30 minutes
    }
    token = jwt.encode(token_payload, app.config['SECRET_KEY'], algorithm='HS256')

    # Return the token as a JSON response
    return jsonify({'token': token, 'user_id': user.id}), 200

@app.route('/protected_route', methods=['GET'])
def protected_route():
    """
    Protect a route with JWT token authorization.
    """
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Authorization token missing.'}), 401
    try:
        # Remove 'Bearer ' prefix from the token
        token = token.replace('Bearer ', '')
        #print(token)
        # Decode the token using the secret key
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])

        # You can now use the payload data, such as user ID, to perform actions
        user_id = payload.get('user_id')

        return jsonify({'message': 'Access granted!', 'user_id': user_id}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired.'}), 403
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token.'}), 401




@app.route('/forgot_password', methods=['POST'])
def forgot_password():
    """
    Initiate the process of password reset.
    """
    data = request.get_json()
    print(data)
    email = data.get('email')
    if not email:
        return jsonify({'error': 'Please enter an email'}), 400
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'error': 'There is no account with that email. You must register first.'}), 400
    token = s.dumps(email, salt='password-reset-link')
    confirm_route = 'reset'
    link = f'{EMAIL_VERIFY_URI}/{confirm_route}/{token}'

    html_content = create_reset_password_body(link)
    msg = Message('reset password', sender=EMAIL_USER, recipients=[email], html=html_content)
    mail.send(msg)

    return jsonify({'success': 'The Password reset link is sent on your mail.'})

@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset(token):
    """
    Reset user password.
    """
    if request.method == 'GET':
        try:
            email = s.loads(token, salt='password-reset-link', max_age=1800)
            # Assuming User is your SQLAlchemy User model
            user = User.query.filter_by(email=email).first()
            # Here, you can render the HTML template for resetting password
            # You can include the new password form here and send it to the frontend
            html_content = password_reset_form_html(token)
            return render_template_string(html_content)
        except Exception as error:
            return str(error)
    elif request.method == 'POST':
        token = request.form.get('token')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        try:
            email = s.loads(token, salt='password-reset-link', max_age=1800)
            user = User.query.filter_by(email=email).first()
            if user:
                if new_password == confirm_password:
                    # Update the user's password and reset token logic here
                    user.password = bcrypt.generate_password_hash(new_password)  # Hash the password
                    # Clear the reset token or set it to None in the database
                    user.reset_token = None
                    db.session.commit()
                    # Return success message or redirect to login page
                    login_url = "http://pdf.bluetickconsultants.com/login.html"
                    html_content = password_reset_success_html(login_url)
                    return render_template_string(html_content)
                else:
                    return "Passwords do not match."
            else:
                return "User not found."
        except Exception:
            return "Link expired or invalid."
    else:
        return "Method not allowed."