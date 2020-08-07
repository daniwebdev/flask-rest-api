# Import flask dependencies
from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from app import app
from app.middleware import require_token
from app.model import User, db
import jwt
import bcrypt


auth_module = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@auth_module.route('/login/', methods=['GET', 'POST'])
@require_token()
def login():
    val = request.values
    user = User.query.filter_by(username=val["username"]).first()
    
    if bcrypt.checkpw(val['password'].encode('utf-8'), user.password):
        
        exp = datetime.now() + timedelta(days=7)

        payload = {
            'exp': exp.timestamp()
        }

        token = jwt.encode(payload, app.config.get('SECRET_KEY'), algorithm='HS256')

        data = {
            "status": True,
            "code": 200,
            "token": str(token)
        }
    else:
        data = {
            "status": False,
            "code": 401,
            "message": "Unauthorized"
        }

    return jsonify(data)


@auth_module.route('/register', methods=['POST'])
def register():

    val = request.values
    salt = bcrypt.gensalt()

    password = bcrypt.hashpw(val['password'].encode('utf-8'), salt)

    create = User()
    create.username = val['username']
    create.email = val['email']
    create.password = password

    db.session.add(create)
    db.session.commit()

    return jsonify(request.values['username'])