from .base_model import BaseDBModel
from .base_repository import BaseRepository

from Domain.gp import GrandPrixDB2DomainConverter


class GrandPrixDBModel(BaseDBModel):
    def __init__(self, id, title, date, vendor_id):
        self.id = id
        self.title = title
        self.date = date
        self.vendor_id = vendor_id


class GrandPrixRepository(BaseRepository):
    def __init__(self, conn):
        self.conn = conn

    def get(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM gps;')
        gps = cursor.fetchall()

        converter = GrandPrixDB2DomainConverter()
        domain_gps = list(map(lambda x: converter.convert(*x), gps))
        return domain_gps
        
    def create(self, domain_model):
        title = domain_model.title
        date = domain_model.date
        vendor_id = domain_model.vendor_id

        cursor = self.conn.cursor()
        try:
            cursor.execute(f'INSERT INTO gps (title, gp_date, vendor_id) VALUES (\'{title}\', \'{date}\', \'{vendor_id}\');')
        except:
            self.conn.rollback()
            raise Exception('ERROR! Transaction failed!')
        self.conn.commit()

    def delete(self, id):
        cursor = self.conn.cursor()
        try:
            cursor.execute(f'DELETE FROM gps WHERE id = {id}')
        except:
            self.conn.rollback()
            raise Exception('ERROR! Transaction failed!')
        self.conn.commit()
        