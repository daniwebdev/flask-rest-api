# Import flask dependencies
from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from app import app
import jwt
from app.middleware import require_token

auth_module = Blueprint('auth', __name__, url_prefix='/auth')


# Set the route and accepted methods
@auth_module.route('/login/', methods=['GET', 'POST'])
@require_token()
def login():
    exp = datetime.now() + timedelta(days=7)
    print(request.user['name'])
    payload = {
        'exp': exp.timestamp()
    }

    token = jwt.encode(payload, app.config.get('SECRET_KEY'), algorithm='HS256')

    data = {
        "token": str(token)
    }

    return jsonify(data)
