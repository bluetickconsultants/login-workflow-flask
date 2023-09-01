import jwt
from flask import jsonify, request
from config import SECRET_KEY
from functools import wraps

def token_required(f):
    """
    Decorator function to require a valid JWT token for authorization.

    Args:
        f (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # JWT token is passed in the request header
        token = request.headers.get('Authorization')
        # Return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401
  
        try:
            # Decoding the payload to fetch the stored details
            token = token.replace('Bearer ', '')
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = data['email']
        except:
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        # Return a success message with the current user's context
        return jsonify({
            'message': 'Token is valid !!' + ' ' + current_user,
        }), 200
  
    return decorated
