"""
Module for Google OAuth2 login routes.
"""

from datetime import datetime
import cachecontrol
import requests
import google.auth.transport.requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from google.auth.exceptions import RefreshError
from flask import session, redirect, request,abort,jsonify
from api import app

# Google OAuth2 configuration
GOOGLE_CLIENT_ID = "your-google-client-id"
GOOGLE_CLIENT_SECRET = "your-google-client-secret"
GOOGLE_SCOPES = ["openid", "profile", "email"]

flow = Flow.from_client_secrets_file(
    "path/to/client_secrets.json",
    scopes=GOOGLE_SCOPES,
    redirect_uri="your-redirect-uri"
)

@app.route("/google_login")
def google_login():
    """
    Redirects the user to the Google OAuth2 authorization URL.
    """
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@app.route("/callback")
def callback():
    """
    Handles the callback from Google OAuth2 authentication.
    """
    try:
        flow.fetch_token(authorization_response=request.url)

        if not session["state"] == request.args["state"]:
            abort(500)  # State does not match!

        credentials = flow.credentials
        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(session=cached_session)

        try:
            id_info = id_token.verify_oauth2_token(
                id_token=credentials._id_token,
                request=token_request,
                audience=GOOGLE_CLIENT_ID
            )
            session["google_id"] = id_info.get("sub")
            session["name"] = id_info.get("name")
            return jsonify({"success":"successfully authorised"})
        except RefreshError as refresh_error:
            if "Token used too early" in str(refresh_error):
                current_time = int(datetime.now().timestamp())
                token_expiration_time = int(credentials.expiry.timestamp())
                if current_time < token_expiration_time:
                    return "Token used too early. Please make sure your computer's clock is set correctly."
            return str(refresh_error)
    except Exception as exception:
        return str(exception)
