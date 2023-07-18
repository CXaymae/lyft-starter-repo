import unittest
from datetime import datetime
#Remove Uneceesary imports
from engine.model.car import car


#Set helper method which contain similar parts of each duplicated functionality methods

   class CarServiceTests(unittest.TestCase):
    #initialize common variables and objects through setUp();
    def setUp(self):
        self.today = datetime.today().date()
        # use relative time calculations based on timedelta from the datetime module
        self.last_service_date = self.today - timedelta(days=365)
        self.current_mileage = 0
        self.last_service_mileage = 0

    def test_battery_service_required(self):
        car = Car(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.needs_service("battery"))

    def test_battery_service_not_required(self):
        car = Car(self.last_service_date - timedelta(days=365), self.current_mileage, self.last_service_mileage)
        self.assertFalse(car.needs_service("battery"))

    def test_engine_service_required(self):
        car = Car(self.last_service_date, self.current_mileage + 30001, self.last_service_mileage)
        self.assertTrue(car.needs_service("engine"))

    def test_engine_service_not_required(self):
        car = Car(self.last_service_date, self.current_mileage + 30000, self.last_service_mileage)
        self.assertFalse(car.needs_service("engine"))


if __name__ == '__main__':
    unittest.main()
