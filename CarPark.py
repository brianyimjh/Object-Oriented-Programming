# Q2 Part a(i)
class CarPark:
    _carHalfHourlyRates = [[700, 1900, 0.6], [1900, 2230, 0.8]]
    _carNightCharge = 5.00
    _motorBikeCharges = [[700, 2230, 0.65]]
    _motorBikeNightCharge = 0.70
    _nextId = 1

    def __init__(self, address):
        """ constructor that execute when an object is created """
        self._address = address
        self._carparkId = type(self)._nextId
        type(self)._nextId += 1  # todo replace the old one with this

    @property
    def address(self):
        return self._address

    @property
    def carparkId(self):
        return self._carparkId

    def getCarHalfHourlyRate(self, aTime):
        """ The method returns a list from _carHalfHourlyRates """
        for rate in type(self)._carHalfHourlyRates:
            if rate[0] <= aTime < rate[1]:
                return rate
        return None

    def getMotorBikeCharge(self, aTime):
        """ The method does the same task as getCarHalfHourlyRate except that method uses the class variable
        _motorBikeCharges """
        for rate in type(self)._motorBikeCharges:
            if rate[0] <= aTime < rate[1]:
                return rate
        return None

    def getCarNightCharge(self):
        """ The method returns the night parking charge for the vehicle type car """
        return type(self)._carNightCharge

    def getMotorBikeNightCharge(self):
        """ The method returns the night parking charge for the vehicle type motorbike """
        return type(self)._motorBikeNightCharge

    def __str__(self):
        """ return the string representation of the object """
        return f"Carpark Id: {self._carparkId}\t{self._address}\t**Outside of Central Area**"
        # todo replace the old one with this