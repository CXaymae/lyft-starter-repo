from engine.engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        # Check if the difference between the current mileage and the last service mileage is greater than 30000
        return self.current_mileage - self.last_service_mileage > 30000
