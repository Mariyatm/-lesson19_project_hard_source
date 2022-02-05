import hashlib
import hmac
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
import base64


def get_password_digest(password):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    )


def get_password_hash(password):
    return base64.b64encode(get_password_digest(password)).decode('utf-8')


def check_password(password_hash, other_password):
    return hmac.compare_digest(
        password_hash,
        get_password_digest(other_password)
    )
