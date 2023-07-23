from battery.battery import Battery
from utils import add_years_to_date


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        # Initialize the NubbinBattery with the current date and the date of the last service
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        # Calculate the date by which the battery should be serviced (4 years after the last service)
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 4)
        
        # Check if the calculated date is before the current date
        if date_which_battery_should_be_serviced_by < self.current_date:
            # If the battery needs servicing, return True
            return True
        else:
            # If the battery does not need servicing, return False
            return False