# Import necessary modules
import unittest

# Import the WilloughbyEngine class from the engine.willoughby_engine module
from engine.willoughby_engine import WilloughbyEngine

# Define the test class that inherits from unittest.TestCase
class TestWilloughbyEngine(unittest.TestCase):
    
    # Test case for the needs_service() method when the engine needs servicing
    def test_needs_service_true(self):
        # Set the current mileage and the mileage of the last service
        current_mileage = 60001
        last_service_mileage = 0
        
        # Create an instance of the WilloughbyEngine class with the provided mileage values
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        
        # Assert that the needs_service() method should return True when the engine needs servicing
        self.assertTrue(engine.needs_service())

    # Test case for the needs_service() method when the engine does not need servicing
    def test_needs_service_false(self):
        # Set the current mileage and the mileage of the last service
        current_mileage = 60000
        last_service_mileage = 0
        
        # Create an instance of the WilloughbyEngine class with the provided mileage values
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        
        # Assert that the needs_service() method should return False when the engine doesn't need servicing
        self.assertFalse(engine.needs_service())