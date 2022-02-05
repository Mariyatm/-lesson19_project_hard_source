import jwt
from flask import request
from flask_restx import abort
from config import Config
from tools.jwt_token import JwtToken, JwtSchema


def login_required(func):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            abort(401)
        try:
            token = auth_header.split("Bearer ")[-1]
            data = JwtToken.decode_token(token)
            data.pop("exp", None)
            token_data = JwtSchema().load(data)
            return func(*args, **kwargs, token_data=token_data)
        except Exception as e:
            print(f"Traceback: {e}")
            abort(401)
    return wrapper

def admin_required(func):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            abort(401)
        try:
            token = auth_header.split("Bearer ")[-1]
            data = JwtToken.decode_token(token)
            token_data = JwtSchema().load(data)
            if token_data["role"] != "admin":
                abort(403)
            return func(*args, **kwargs, token_data=token_data)
        except Exception as e:
            print(f"Traceback: {e}")
            abort(401)
    return wrapper