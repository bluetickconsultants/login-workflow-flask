##Login Workflow Flask
This project provides a complete login workflow including user registration, email verification, login, password recovery, and Google login functionality.
##Project Structure
project_folder/
|-- api/
|   |-- authentication/
|   |   |-- auth.py
|   |   |-- models.py
|   |   |-- google_auth.py
|-- tests/
|   |-- test_authentication.py
|-- utils/
|   |-- email_templates.py
|   |-- google_login_utils.py
|-- config.py
|-- app.py
|-- Makefile
|-- README.md
|-- requirements.txt
|-- .gitignore

##Components
api/authentication: Contains authentication-related functionality.

auth.py: Defines authentication routes and logic.
models.py: Defines the User model and database schema.
google_auth.py: Implements Google login functionality.
tests: Contains unit tests for the authentication functionality.

test_authentication.py: Unit tests for the authentication routes.
utils: Contains utility files.

email_templates.py: Provides email templates for verification and password reset emails.
google_login_utils.py: Contains utilities for implementing Google login.

##Configuration
config.py: Configuration file for various settings like database URLs, email settings, etc.

##App Entry Point
app.py: Main entry point of the application, initializes the Flask app and sets up routes.

##Build and Run
Makefile: Provides commands to build and run the application.

##Usage
Install required packages using pip install -r requirements.txt.
Configure the settings in config.py such as database URLs, email settings, etc.
Run tests using make test.
Start the Flask app using make run.

##Contributing
Fork the repository.
Create a new branch for your feature.
Implement your changes.
Submit a pull request for review.