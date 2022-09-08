from Parking import Parking
from CarParkingCalculator import CarParkingCalculator

# Q3 Part b(iii)
class CarParking(Parking):
    _calculator = CarParkingCalculator()

    def __str__(self):
        return f"{super().__str__()} Car"