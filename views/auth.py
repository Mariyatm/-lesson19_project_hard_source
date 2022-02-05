from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import ValidationError

from implemented import user_service
from tools.jwt_token import JwtSchema, JwtToken
from views.users import LoginValidator

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        try:
            data = LoginValidator().load(request.json)
            user = user_service.get_by_name(data["username"])
            if not user:
                abort(404)
            token_data = JwtSchema().load({"user_id": user.id, "role": user.role})
            return JwtToken(token_data).get_tokens(), 201
        except ValidationError:
            abort(400)

    def put(self):
        try:
            refresh_token = request.json["refresh_token"]
            data = JwtToken.decode_token(refresh_token)
            data.pop("exp", None)
            token_data = JwtSchema().load(data)
            user = user_service.get_one(token_data["user_id"])
            if not user:
                abort(404)
            token_data = JwtSchema().load({"user_id": user.id, "role": user.role})
            return JwtToken(token_data).get_tokens(), 201
        except Exception as e:
            abort(400)
