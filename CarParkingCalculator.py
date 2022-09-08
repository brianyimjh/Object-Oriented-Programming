from ParkingCalculator import ParkingCalculator

# Q2 Part b(iii)
class CarParkingCalculator(ParkingCalculator):
    def getDayRate(self, startTime, carpark):
        """ The method gets the day rate in the form of [a, b, c] for motorcycle for a given time from the carpark """
        return carpark.getCarHalfHourlyRate(startTime)

    def getNightRate(self, carpark):
        """ The method gets the night rate for motorcycle from the carpark """
        return carpark.getCarNightCharge()

    def getCharge(self, endTime, startTime, rate):
        """ The method returns the charges for parking for a given period between a start time and an end time on a
        per period basis """
        charge = 0.00

        period = endTime - startTime
        minutes = period.seconds // 60

        noOf30MinuteBlock = minutes // 30
        if minutes % 30 != 0:  # any part of 30 minutes
            noOf30MinuteBlock += 1

        charge += (noOf30MinuteBlock * rate)
        return charge