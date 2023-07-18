from abc import ABC
from car import Car

#direct inheritence from Car and ABC using multiple inheritances.
class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on

