from ParkingCalculator import ParkingCalculator

# Q2 Part b(ii)
class MotorbikeParkingCalculator(ParkingCalculator):
    def getDayRate(self, startTime, carpark):
        """ The method gets the day rate in the form of [a, b, c] for motorcycle for a given time from the carpark """
        return carpark.getMotorBikeCharge(startTime)

    def getNightRate(self, carpark):
        """ The method gets the night rate for motorcycle from the carpark """
        return carpark.getMotorBikeNightCharge()

    def getCharge(self, endTime, startTime, rate):
        """ The method returns the charges for parking for a given period between a start time and an end time on a
        per period basis """
        charge = 0.00

        charge += rate
        return charge