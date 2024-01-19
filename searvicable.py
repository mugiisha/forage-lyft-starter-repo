from abc import ABC, abstractmethod


class Searvicable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
