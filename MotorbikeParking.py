from Parking import Parking
from MotorbikeParkingCalculator import MotorbikeParkingCalculator


# Q3 Part b(ii)
class MotorbikeParking(Parking):
    _calculator = MotorbikeParkingCalculator()

    def __str__(self):
        return f"{super().__str__()} Motor Bike"