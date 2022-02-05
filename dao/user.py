from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(User).get(id)

    def get_by_name(self, name):
        return self.session.query(User).filter(User.username == name).one_or_none()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update_role(self, name, role):
        user = self.get_by_name(name)
        user.role = role
        self.session.add(user)
        self.session.commit()

    def update_pass_hash(self, name, phash):
        user = self.get_by_name(name)
        user.password = phash
        self.session.add(user)
        self.session.commit()
