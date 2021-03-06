from DTO.base_dto import BaseDTO


class TicketDTO(BaseDTO):
    def __init__(self, id, price, session, gp_id, in_stock, username):
        super().__init__(id)
        self.price = price
        self.session = session
        self.gp_id = gp_id
        self.in_stock = in_stock
        self.vendor_name = username
    
    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "session": self.session,
            "gp_id": self.gp_id,
            "vendor_name": self.vendor_name,
            "in_stock": self.in_stock,
        }
