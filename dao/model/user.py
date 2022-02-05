from marshmallow import Schema, fields
from setup_db import db
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
import hashlib


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.String)
    #
    # def get_hash(password):
    #     return hashlib.pbkdf2_hmac(
    #         'sha256',
    #         password.encode('utf-8'),  # Convert the password to bytes
    #         PWD_HASH_SALT,
    #         PWD_HASH_ITERATIONS
    #     ).decode("utf-8", "ignore")


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
