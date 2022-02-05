from dao.user import UserDAO
from tools.security import get_password_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, id):
        return self.dao.get_one(id)

    def get_by_name(self, name):
        return self.dao.get_by_name(name)

    def create(self, username, password, role="user"):
        return self.dao.create(
            {"username": username,
             "password": get_password_hash(password),
             "role": role
             })

    def update_role(self, role):
        self.update_role(role)

    def update_password(self, password):
        pass
