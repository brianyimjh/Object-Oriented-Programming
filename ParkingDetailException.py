from ParkingException import ParkingException


# Q3 Part a(ii)
class ParkingDetailException(ParkingException):
    def __init__(self, message, parking):
        super().__init__(message)
        self._parking = parking

    @property
    def parking(self):
        return self._parking