import psycopg2 as db

from .user import UserRepository
from .gp import GrandPrixRepository
from .ticket import TicketRepository


class RepositoryFactory:
    # conn = None
    def __init__(self, port, readonly):
        conn = db.connect(
            host="localhost",
            port=f"{port}",
            database="bmstu_web_f1",
            user="postgres",
            password="ImSuperUser12"
        )
        self.conn = conn
        conn.set_session(readonly=readonly)
    
    def create_user_repository(self):
        return UserRepository(self.conn)

    def create_gp_repository(self):
        return GrandPrixRepository(self.conn)

    def create_ticket_repository(self):
        return TicketRepository(self.conn)
