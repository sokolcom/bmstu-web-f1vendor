from abc import ABC, abstractmethod


class BaseDTO(ABC):
    def __init__(self, id):
        self.id = id

    @abstractmethod
    def to_dict(self):
        pass
