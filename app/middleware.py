from functools import wraps
from flask import request
from app import app


def require_token():
    def _require_token(f):
        @wraps(f)
        def __require_token(*args, **kwargs):
            # just do here everything what you need
            print(request.headers)
            request.user = {
                "name": "Dani"
            }

            result = f(*args, **kwargs)

            return result

        return __require_token

    return _require_token
