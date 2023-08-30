
# Login Workflow

This project provides a complete login workflow including user registration, email verification, login, password recovery, and Google login functionality


## Components
api/authentication: Contains authentication-related functionality.

auth.py: Defines authentication routes and logic. 
models.py: Defines the User model and database schema. 
google_auth.py: Implements Google login functionality.
test_authentication.py: Unit tests for the authentication routes. 
utils: Contains utility files.
email_templates.py: Provides email templates for verification and password reset emails.


## Configuration

config.py: Configuration file for various settings like database URLs, email settings, etc.

app.py: Main entry point of the application, initializes the Flask app and sets up routes.

## Usage

Install required packages using pip install -r requirements.txt. Configure the settings in config.py such as database URLs, email settings, etc. Run tests using make test. Start the Flask app using make run.

