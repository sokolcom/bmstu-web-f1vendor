from .base_model import BaseDBModel
from .base_repository import BaseRepository

from Domain.user import UserDB2DomainConverter


class UserDBModel(BaseDBModel):
    def __init__(self, id, username, pwrd, role):
        self.id = id
        self.username = username
        self.password = pwrd
        self.role = role


class UserRepository(BaseRepository):
    def __init__(self, conn):
        self.conn = conn

    def get(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * from users;')
        users = cursor.fetchall()

        converter = UserDB2DomainConverter()
        domain_users = list(map(lambda x: converter.convert(UserDBModel(*x)), users))
        return domain_users

    def create(self, domain_user):
        username = domain_user.username
        password = domain_user.password
        role = domain_user.role

        cursor = self.conn.cursor()
        try:
            cursor.execute(f'INSERT INTO users (username, pswrd, user_role) VALUES (\'{username}\', \'{password}\', \'{role}\');')
        except:
            self.conn.rollback()
            raise Exception('ERROR! Transaction failed!')
        self.conn.commit()
    
    def delete(self, id):
        cursor = self.conn.cursor()
        try:
            cursor.execute(f'DELETE FROM users WHERE id = {id}')
        except:
            self.conn.rollback()
            raise Exception('ERROR! Transaction failed!')
        self.conn.commit()
        
