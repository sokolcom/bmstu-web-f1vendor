from abc import ABC, abstractmethod


class BaseEntity(ABC):
    @abstractmethod
    def __init__(self):
        pass


class BaseDomain2DTOConverter(ABC):
    @abstractmethod
    def convert(self):
        pass


class BaseDTO2DomainConverter(ABC):
    @abstractmethod
    def cobvert(self):
        pass


class BaseDB2DomainConverter(ABC):
    @abstractmethod
    def convert(self):
        pass
