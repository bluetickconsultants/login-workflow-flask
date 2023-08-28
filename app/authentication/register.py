from flask import jsonify, render_template_string, request
import datetime
from app import db, mail,bcrypt,s,app
from flask_mail import Mail, Message
from app.authentication.models import User
from utils.login_utils import create_verification_email_body,email_verified_success_html

EMAIL_USER = app.config['MAIL_USERNAME'] 
EMAIL_PASS = app.config['MAIL_PASSWORD'] 
EMAIL_VERIFY_URI = app.config['EMAIL_VERIFY_URI']


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method=='POST':
        data = request.get_json()
        print(data)
        email = data.get('email')
        password = data.get('password')

        # Check if email and password are provided in the request body
        if not email  or not password:
            return jsonify({'error': 'Email and password are required.'}), 400
        existing_user_email = User.query.filter_by(email=email).first()
        if existing_user_email:
            return jsonify({'error': 'Email already exists.'}), 401
        else:
            try:
                password_encoded = password.encode('utf-8')
                hashed_password = bcrypt.generate_password_hash(password_encoded)
                # print("Hashed Password during registration:", hashed_password)
                new_user = User(email=email, password=hashed_password)
                
                db.session.add(new_user)
                db.session.commit()
                
                token = s.dumps(email, salt='email-confirmation-link')
                confirm_route = 'confirm'
                link = f'{EMAIL_VERIFY_URI}/{confirm_route}/{token}'

                html_content = create_verification_email_body(link)
                
                msg = Message('verification',sender=EMAIL_USER,recipients=[email],html=html_content)
                
                # print(link)
                
                mail.send(msg) 
                # print(msg)              
                
                return jsonify({"message": "created user successfully"}), 200
            except Exception as e:
                db.session.rollback()
                return jsonify({'error': e}), 401
            
@app.route('/confirm/<token>')
def confirm(token):
    try:
        email = s.loads(token, salt='email-confirmation-link', max_age=1800)
        user = User.query.filter_by(email=email).first()
        if user:
            user.email_confirmed = True
            user.email_confirmed_on = datetime.datetime.now()
            db.session.commit()
                        # Return HTML code with a button that redirects to the login page
            # Generate the correct URL for the login page
            login_url = "http://pdf.bluetickconsultants.com/login.html"
            
            # Return HTML code with a button that redirects to the login page
            html_content = email_verified_success_html(login_url)
            
            return render_template_string(html_content)
        else:
            return "User not found."
    except Exception:
        return "Link expired or invalid."