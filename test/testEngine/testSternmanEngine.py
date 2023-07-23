# Import necessary modules
import unittest

# Import the SternmanEngine class from the engine.sternman_engine module
from engine.sternman_engine import SternmanEngine

# Define the test class that inherits from unittest.TestCase
class TestSternmanEngine(unittest.TestCase):
    
    # Test case for the needs_service() method when the engine needs servicing
    def test_needs_service_true(self):
        # Set the warning light status to True, indicating it is on
        warning_light_is_on = True
        
        # Create an instance of the SternmanEngine class with the provided warning light status
        engine = SternmanEngine(warning_light_is_on)
        
        # Assert that the needs_service() method should return True when the engine needs servicing
        self.assertTrue(engine.needs_service())

    # Test case for the needs_service() method when the engine does not need servicing
    def test_needs_service_false(self):
        # Set the warning light status to False, indicating it is off
        warning_light_is_on = False
        
        # Create an instance of the SternmanEngine class with the provided warning light status
        engine = SternmanEngine(warning_light_is_on)
        
        # Assert that the needs_service() method should return False when the engine doesn't need servicing
        self.assertFalse(engine.needs_service())
