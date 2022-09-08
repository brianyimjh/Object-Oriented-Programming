# Q2 Part a(ii)

from CarPark import CarPark


class CentralAreaCarPark(CarPark):
    _nightParkingSurcharge = 2.00
    _carHalfHourlyRates = [[700, 1700, 1.2], [1700, 2230, 0.9]]
    _factorChange = 1  # make sure adjustment made based on factor is only once

    def __init__(self, factor, address):
        """ constructor that execute when an object is created """
        super().__init__(address)
        self._factor = factor

    @classmethod
    def nightParkingSurcharge(cls):
        return cls._nightParkingSurcharge

    @classmethod
    def nightParkingSurcharge(cls, nightParkingSurcharge):
        cls._nightParkingSurcharge = nightParkingSurcharge

    @property
    def factor(self):
        return self._factor

    @factor.setter
    def factor(self, factor):
        type(self)._factorChange = 1  # make sure adjustment made based on factor is only once if new factor is set
        self._factor = factor

    def getCarNightCharge(self):
        """ The method adds the surcharge for night parking to the night charge for the superclass """
        return super().getCarNightCharge() + type(self)._nightParkingSurcharge

    def getCarHalfHourlyRate(self, aTime):
        """ The method adjusts the rate by multiplying it with the factor before returning the list """
        if type(self)._factorChange == 1:
            for rate in type(self)._carHalfHourlyRates:
                rate[2] *= self._factor
            type(self)._factorChange -= 1  # make sure adjustment made based on factor is only once
            return super().getCarHalfHourlyRate(aTime)
        return super().getCarHalfHourlyRate(aTime)  # if adjustment based on factor has been made before, simply
        # return list

    def __str__(self):
        """ return the string representation of the object """
        return f"Carpark Id: {self._carparkId}\tFactor: {self._factor}\t{self._address}\t**Within Central Area**"
        # todo replace the old one with this
