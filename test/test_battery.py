import unittest
from datetime import datetime

from car_factory import CarFactory

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        rorschach = CarFactory.create_rorschach(today,last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(rorschach.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0

        rorschach = CarFactory.create_rorschach(today,last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(rorschach.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False

        pallindrome = CarFactory.create_palindrome(today,last_service_date,warning_light_is_on)
        self.assertTrue(pallindrome.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year)
        warning_light_is_on = False

        pallindrome = CarFactory.create_palindrome(today,last_service_date,warning_light_is_on)
        self.assertFalse(pallindrome.needs_service())

if __name__ == '__main__':
    unittest.main()