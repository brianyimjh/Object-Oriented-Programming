from abc import ABC, abstractmethod
from ParkingException import ParkingException


# Q3 Part b(i)
class Parking(ABC):
    _calculator = None

    def __init__(self, timeIn, vehicleNumber, carpark):
        """ constructor that execute when an object is created """
        self._timeIn = timeIn
        self._vehicleNumber = vehicleNumber
        self._carpark = carpark
        self._timeOut = None
        self._charges = 0

    @property
    def timeIn(self):
        return self._timeIn

    @property
    def vehicleNumber(self):
        return self._vehicleNumber

    @property
    def carpark(self):
        return self._carpark

    @property
    def timeOut(self):
        return self._timeOut

    @property
    def charges(self):
        if self._timeOut is None:
            raise ParkingException("Charges not recorded yet as vehicle has not left carpark.")
        return self._charges

    @timeOut.setter
    def timeOut(self, timeOut):
        if self._timeOut is not None:
            raise ParkingException("Time out has already been recorded!")

        if timeOut < self._timeIn:
            raise ParkingException("Time out cannot be earlier than time in!")

        self._timeOut = timeOut
        self._charges = type(self)._calculator.calculateCharges(self._timeIn, self._timeOut, self._carpark)

    def __str__(self):
        """ return the string representation of the object """
        if self._timeOut is None:
            timeIn = self._timeIn.strftime("%d %b %Y, %I:%M %p")
            return f"Time In: {timeIn}\tTime Out: *Parked in carpark {self._carpark.carparkId}*\tCharges: ${self._charges:.2f}\n{self._carpark.__str__()}\nVehicle: {self._vehicleNumber}"

        else:
            timeIn = self._timeIn.strftime("%d %b %Y, %I:%M %p")
            timeOut = self._timeOut.strftime("%d %b %Y, %I:%M %p")
            return f"Time In: {timeIn}\tTime Out: {timeOut}\tCharges: ${self._charges:.2f}\n{self._carpark.__str__()}\nVehicle: {self._vehicleNumber}"