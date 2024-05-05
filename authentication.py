from functools import wraps
from flask import jsonify,request

def authenticate_request(request):
    # Extracting authentication credentials from the request (e.g., API key, token)
    auth_header = request.headers.get('Authorization')
    auth_data = auth_header.split()
    
    if len(auth_data) != 2 or auth_data[0] != 'Bearer':
        return False
    
    token = auth_data[1]

    # Performing authentication logic (e.g., validate token against database)
    if token == 'dummy_token':
        return True
    else:
        return False

# Defining a custom authentication decorator
def authenticate(func):
    @wraps(func) # Preserve the original function name
    def wrapper(*args, **kwargs):
        # Calling the authentication function with the request object
        authenticated = authenticate_request(request)
        if not authenticated:
            return jsonify({'error': 'Authentication failed'}), 401
        return func(*args, **kwargs)
    return wrapper

