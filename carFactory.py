from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        # Create a CapuletEngine with the provided current and last service mileage
        engine = CapuletEngine(current_mileage, last_service_mileage)
        
        # Create a SpindlerBattery with the provided current and last service dates
        battery = SpindlerBattery(current_date, last_service_date)
        
        # Create a Car instance with the engine and battery
        car = Car(engine, battery)
        
        # Return the created Car instance
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        # Create a WilloughbyEngine with the provided current and last service mileage
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        
        # Create a SpindlerBattery with the provided current and last service dates
        battery = SpindlerBattery(current_date, last_service_date)
        
        # Create a Car instance with the engine and battery
        car = Car(engine, battery)
        
        # Return the created Car instance
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        # Create a SternmanEngine with the provided warning light status
        engine = SternmanEngine(warning_light_is_on)
        
        # Create a SpindlerBattery with the provided current and last service dates
        battery = SpindlerBattery(current_date, last_service_date)
        
        # Create a Car instance with the engine and battery
        car = Car(engine, battery)
        
        # Return the created Car instance
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        # Create a WilloughbyEngine with the provided current and last service mileage
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        
        # Create a NubbinBattery with the provided current and last service dates
        battery = NubbinBattery(current_date, last_service_date)
        
        # Create a Car instance with the engine and battery
        car = Car(engine, battery)
        
        # Return the created Car instance
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        # Create a CapuletEngine with the provided current and last service mileage
        engine = CapuletEngine(current_mileage, last_service_mileage)
        
        # Create a NubbinBattery with the provided current and last service dates
        battery = NubbinBattery(current_date, last_service_date)
        
        # Create a Car instance with the engine and battery
        car = Car(engine, battery)
        
        # Return the created Car instance
        return car