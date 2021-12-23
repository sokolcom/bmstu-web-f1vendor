from Domain.base_domain import BaseEntity, BaseDB2DomainConverter


class User(BaseEntity):
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


class UserDB2DomainConverter(BaseDB2DomainConverter):
    def convert(self, db_model):
        return User(
            db_model.username,
            db_model.password,
            db_model.role
        )
