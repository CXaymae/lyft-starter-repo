# Import necessary modules
import unittest
from datetime import date

# Import the SpindlerBattery class from the battery.spindler_battery module
from battery.spindler_battery import SpindlerBattery

# Define the test class that inherits from unittest.TestCase
class TestSpindlerBattery(unittest.TestCase):
    
    # Test case for the needs_service() method when the battery needs servicing
    def test_needs_service_true(self):
        # Set the current date and the date of the last service
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        
        # Create an instance of the SpindlerBattery class with the provided dates
        battery = SpindlerBattery(current_date, last_service_date)
        
        # Assert that the needs_service() method should return True when the battery needs servicing
        self.assertTrue(battery.needs_service())

    # Test case for the needs_service() method when the battery does not need servicing
    def test_needs_service_false(self):
        # Set the current date and the date of the last service
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        
        # Create an instance of the SpindlerBattery class with the provided dates
        battery = SpindlerBattery(current_date, last_service_date)
        
        # Assert that the needs_service() method should return False when the battery doesn't need servicing
        self.assertFalse(battery.needs_service())
