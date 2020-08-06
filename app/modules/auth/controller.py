# Import flask dependencies
from flask import Blueprint, request

auth_module = Blueprint('auth', __name__, url_prefix='/auth')
# Set the route and accepted methods
@auth_module.route('/signin/', methods=['GET', 'POST'])
def signin():
    return request.method