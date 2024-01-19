import unittest
from datetime import datetime
from tire.octoprime_tires import OctoprimeTire
from tire.carrigan_tires import CarriganTire

class TestCarigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear_array = [0.1,0.2,0.3,0.9]
        carigan= CarriganTire(tire_wear_array)
        self.assertTrue(carigan.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear_array = [0.1,0.2,0.3,0.5]
        carigan= CarriganTire(tire_wear_array)
        self.assertFalse(carigan.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear_array = [0.9,0.9,0.9,0.9]
        octoprime= OctoprimeTire(tire_wear_array)
        self.assertTrue(octoprime.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear_array = [0.1,0.2,0.3,0.5]
        octoprime= OctoprimeTire(tire_wear_array)
        self.assertFalse(octoprime.needs_service())