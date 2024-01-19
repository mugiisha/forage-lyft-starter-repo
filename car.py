from abc import ABC, abstractmethod
from searvicable import Searvicable

class Car(Searvicable,ABC):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
