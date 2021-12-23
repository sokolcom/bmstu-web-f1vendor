from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def delete(self):
        pass