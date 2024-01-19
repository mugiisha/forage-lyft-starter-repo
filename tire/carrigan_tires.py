from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear_array):
        self.tire_wear_array = tire_wear_array

    def needs_service(self):
        count = 0
        for tire_wear in self.tire_wear_array:
            if tire_wear >= 0.9:
                count += 1
        return count >= 1