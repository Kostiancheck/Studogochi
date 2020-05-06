from abc import ABC, abstractmethod


class IDraw(ABC):
    @abstractmethod
    def draw(self):
        pass
