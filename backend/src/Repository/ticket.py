from .base_model import BaseDBModel
from .base_repository import BaseRepository

from Domain.ticket import TicketDB2DomainConverter


class TicketDBModel(BaseDBModel):
    def __init__(self, id, title, date, vendor_id):
        self.id = id
        self.title = title
        self.date = date
        self.vendor_id = vendor_id


class TicketRepository(BaseRepository):
    def __init__(self, conn):
        self.conn = conn

    def get(self, id=None, gp_id=None):
        cursor = self.conn.cursor()

        if id is not None:
            cursor.execute(
                f'SELECT t.*, u.username \
                FROM tickets t JOIN gps g ON t.gp_id = g.id JOIN users u on g.vendor_id = u.id \
                WHERE t.id = {id};'
            )
            tickets = cursor.fetchall()
        elif gp_id is not None:
            cursor.execute(
                f'SELECT t.*, u.username \
                FROM tickets t JOIN gps g ON t.gp_id = g.id JOIN users u on g.vendor_id = u.id \
                WHERE t.gp_id = {gp_id};'
            )
            tickets = cursor.fetchall()

        converter = TicketDB2DomainConverter()
        domain_tickets = list(map(lambda x: converter.convert(*x), tickets))
        return domain_tickets
        
    def create(self, domain_model):
        price = domain_model.price
        session = domain_model.session
        gp_id = domain_model.gp_id

        cursor = self.conn.cursor()
        try:
            cursor.execute(f'INSERT INTO tickets (price, gp_session, gp_id) VALUES (\'{price}\', \'{session}\', \'{gp_id}\');')
        except:
            self.conn.rollback()
            raise Exception('ERROR! Transaction failed!')
        self.conn.commit()

    def delete(self, id):
        cursor = self.conn.cursor()
        try:
            cursor.execute(f'DELETE FROM tickets WHERE id = {id}')
        except:
            self.conn.rollback()
            raise Exception('ERROR! Transaction failed!')
        self.conn.commit()

    def buy(self, ticket_id):
        cursor = self.conn.cursor()
        try:
            cursor.execute(f'UPDATE tickets SET in_stock = false WHERE id = {ticket_id}')
        except:
            self.conn.rollback()
            raise Exception('ERROR! Transaction failed!')
        self.conn.commit()
        