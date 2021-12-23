from DTO.base_dto import BaseDTO


class GrandPrixDTO(BaseDTO):
    def __init__(self, id, title, date, vendor_id):
        super().__init__(id)
        self.title = title
        self.date = date
        self.vendor_id = vendor_id
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "vendor_id": self.vendor_id,
        }
