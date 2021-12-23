from abc import ABC, abstractmethod


class BaseDBModel(ABC):
    @abstractmethod
    def __init__(self):
        pass