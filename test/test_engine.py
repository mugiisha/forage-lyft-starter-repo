import unittest
from datetime import datetime

from car_factory import CarFactory

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 5000
        last_service_mileage = 1000

        calliope = CarFactory.create_calliope(today,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(calliope.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 2000
        last_service_mileage = 1000

        calliope = CarFactory.create_calliope(today,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(calliope.needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = True

        pallindrome = CarFactory.create_palindrome(today,last_service_date,warning_light_is_on)
        self.assertTrue(pallindrome.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False

        pallindrome = CarFactory.create_palindrome(today,last_service_date,warning_light_is_on)
        self.assertFalse(pallindrome.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 200000
        last_service_mileage=5000

        glissade = CarFactory.create_glissade(today,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(glissade.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 7000
        last_service_mileage=5000

        glissade = CarFactory.create_glissade(today,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(glissade.needs_service())

if __name__ == '__main__':
    unittest.main()