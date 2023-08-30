from api.authentication.auth import app
from api.authentication.models import db


if __name__ == "__main__":
    # Initialize extensions
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
