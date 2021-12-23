from Domain.base_domain import BaseEntity, BaseDomain2DTOConverter, BaseDB2DomainConverter

from DTO.ticket import TicketDTO


class Ticket(BaseEntity):
    def __init__(self, id, price, session, gp_id, in_stock):
        self.id = id
        self.price = price
        self.session = session
        self.gp_id = gp_id
        self.in_stock = in_stock


class TicketDB2DomainConverter(BaseDB2DomainConverter):
    def convert(self, *args):
        return Ticket(*args)


class TicketDomain2DTOConverter(BaseDomain2DTOConverter):
    def convert(self, domain_model):
        return TicketDTO(
            domain_model.id,
            domain_model.price,
            domain_model.session,
            domain_model.gp_id,
            domain_model.in_stock,
        )
