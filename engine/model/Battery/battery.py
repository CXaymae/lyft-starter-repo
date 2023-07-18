#import the ABC class from the abc module.
from abc import ABC
#By inheriting from ABC, the Battery class becomes an abstract base class
class Battery(ABC):
    #By not providing an implementation, it becomes an abstract method.
    def needs_service(self):
        pass