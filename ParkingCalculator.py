from abc import ABC, abstractmethod
from datetime import datetime


# Q2 Part b(i)
class ParkingCalculator(ABC):

    @abstractmethod
    def getDayRate(self, startTime, carpark):
        pass

    @abstractmethod
    def getNightRate(self, carpark):
        pass

    @abstractmethod
    def getCharge(self, endTime, startTime, rate):
        pass

    def calculateCharges(self, timeIn, timeOut, carpark):
        totalCharge = 0.00
        loopCount = 0

        while timeIn != timeOut:  # as long as timeIn is not equal to timeOut, it will continue to loop

            # separating timeIn and timeOut into the day, month, year, hour, minute
            startTimeDay = timeIn.day
            startTimeMonth = timeIn.month
            startTimeYear = timeIn.year
            startTimeHour = timeIn.hour
            startTimeMinute = timeIn.minute

            endTimeHour = timeOut.hour
            endTimeMinute = timeOut.minute

            # padding 0 to single digit numbers
            if len(str(startTimeHour)) < 2:
                startTimeHour = "0" + str(startTimeHour)
            if len(str(endTimeHour)) < 2:
                endTimeHour = "0" + str(endTimeHour)

            if len(str(startTimeMinute)) < 2:
                startTimeMinute = "0" + str(startTimeMinute)
            if len(str(endTimeMinute)) < 2:
                endTimeMinute = "0" + str(endTimeMinute)

            # getting startTime and endTime for rate
            startTime = int(str(startTimeHour) + str(startTimeMinute))
            endTime = int(str(endTimeHour) + str(endTimeMinute))

            # If the vehicle is in the carpark for l0 minutes or less, there is no charge for the
            # 10 minutes.
            if (timeOut - timeIn).days == 0 and ((timeOut - timeIn).seconds // 60) <= 10 and loopCount == 0:
                return totalCharge

            dayRate = self.getDayRate(startTime, carpark)

            # if dayRate is None but there's a difference in day, means charge is simply night charge
            if dayRate is None:
                if timeOut.day - timeIn.day != 0:
                    rate = self.getNightRate(carpark)
                    totalCharge += rate
                    startTimeDay += 1  # increase startTimeDay by 1 as the night passes
                    startTime = 700  # set startTime to the start of new day
                else:
                    rate = self.getNightRate(carpark)
                    totalCharge += rate
                    startTime = endTime  # startTime becomes the endTime

            else:
                # if no difference in day and endTime is in the same period as startTime, find the difference between
                # the time and the endTime
                if timeOut.day - timeIn.day == 0 and dayRate[0] <= endTime <= dayRate[1]:
                    rate = dayRate[2]
                    timeIn = datetime(startTimeYear, startTimeMonth, startTimeDay, startTime // 100, startTime % 100)
                    # dateTimeIn object to get charge
                    charge = self.getCharge(timeOut, timeIn, rate)
                    totalCharge += charge
                    startTime = endTime  # startTime becomes the endTime

                # if there is a difference in day, find the difference between the time and the end of the hourly
                # rate period
                else:
                    endPeriod = dayRate[1]
                    rate = dayRate[2]

                    timeIn = datetime(startTimeYear, startTimeMonth, startTimeDay, startTime // 100, startTime % 100)
                    # dateTimeIn object to get charge
                    endPeriodTime = datetime(startTimeYear, startTimeMonth, startTimeDay, endPeriod // 100, endPeriod % 100)
                    # dateTimeOut object to get charge

                    charge = self.getCharge(endPeriodTime, timeIn, rate)
                    totalCharge += charge
                    startTime = endPeriod  # startTime becomes the end of the hourly rate period

            startTimeHour = startTime // 100  # get startTimeHour from startTime
            startTimeMinute = startTime % 100  # get startTimeMinute from startTime

            # new timeIn for the comparison of while loop
            timeIn = datetime(startTimeYear, startTimeMonth, startTimeDay, startTimeHour, startTimeMinute)

            loopCount += 1

        return totalCharge