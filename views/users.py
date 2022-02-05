from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import Schema, fields, ValidationError

from dao.model.user import UserSchema
from implemented import user_service
from tools.auth import login_required

user_ns = Namespace('users')


class LoginValidator(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    role = fields.Str()
    # exp = fields.Float()


@user_ns.route('/')
class UserView(Resource):
    @login_required
    def get(self, token_data):
        return UserSchema().dump(user_service.get_one(token_data["user_id"]))

    def post(self):
        try:
            data = LoginValidator().load(request.json)
            user_service.create(**data)
        except ValidationError:
            abort(400)

