import unittest
from api.authentication.auth import app
from api.authentication.models import db


class AuthenticationTestCase(unittest.TestCase):
    """
    Test case for authentication functionality.
    """

    def setUp(self):
        """
        Set up test environment before each test method.
        """
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

        self.app = app.test_client()

        # Push an application context
        self.app_context = app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self):
        """
        Clean up after each test method.
        """
        db.session.remove()
        db.drop_all()

        # Pop the application context
        self.app_context.pop()

    def test_register(self):
        """
        Test user registration.
        """
        data = {"email": "test@example.com", "password": "testpassword"}
        response = self.app.post("/register", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "User created successfully"})

    def test_login(self):
        """
        Test user login.
        """
        data = {"email": "test@example.com", "password": "testpassword"}
        self.app.post("/register", json=data)
        response = self.app.post("/login", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json)
        self.assertIn("user_id", response.json)


if __name__ == "__main__":
    unittest.main()
