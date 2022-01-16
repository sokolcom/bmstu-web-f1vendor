from Domain.base_domain import BaseEntity, BaseDB2DomainConverter


class User(BaseEntity):
    def __init__(self, user_id, username, password, role):
        self.id = user_id
        self.username = username
        self.password = password
        self.role = role


class UserDB2DomainConverter(BaseDB2DomainConverter):
    def convert(self, db_model):
        return User(
            db_model.id,
            db_model.username,
            db_model.password,
            db_model.role
        )
