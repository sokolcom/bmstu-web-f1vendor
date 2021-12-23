from Domain.base_domain import BaseEntity, BaseDomain2DTOConverter, BaseDB2DomainConverter

from DTO.gp import GrandPrixDTO


class GrandPrix(BaseEntity):
    def __init__(self, id, title, date, vendor_id):
        self.id = id
        self.title = title
        self.date = date
        self.vendor_id = vendor_id


class GrandPrixDB2DomainConverter(BaseDB2DomainConverter):
    def convert(self, *args):
        return GrandPrix(*args)


class GrandPrixDomain2DTOConverter(BaseDomain2DTOConverter):
    def convert(self, domain_model):
        return GrandPrixDTO(
            domain_model.id,
            domain_model.title,
            domain_model.date,
            domain_model.vendor_id
        )
