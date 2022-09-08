from datetime import datetime

from CarPark import CarPark
from CentralAreaCarPark import CentralAreaCarPark

from CarParkingCalculator import CarParkingCalculator
from MotorbikeParkingCalculator import MotorbikeParkingCalculator

from CarParking import CarParking
from MotorbikeParking import MotorbikeParking

from CarParkTrackingSystem import CarParkTrackingSystem

from ParkingException import ParkingException
from ParkingDetailException import ParkingDetailException


# todo replace the old one with this
def getIntegerRange(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))

            if min <= value <= max:
                return value
            else:
                print(f"Please re-enter within range")
        except:
            print("The input is not a number")


def menuOption():
    print("Menu")
    print("1. Park a Vehicle")
    print("2. Exit Carpark")
    print("3. Display Parking Summary for all Carparks")
    print("0. Quit")
    option = getIntegerRange("Enter choice: ", 0, 3)
    return option


# Q3 Part d(i)
def parkAVehicle(carparkTrackingSystem):
    print("Park a Vehicle selected")
    try:
        vehicleType = int(input("Enter type of parking 1 - Car 2 - Motor bike: "))
        if vehicleType not in range(1, 2 + 1):
            raise ParkingException("Parking type is not a correct parking type.")

        carparkId = int(input("Enter carpark id: "))
        if carparkTrackingSystem.searchCarParkById(carparkId) is None:
            raise ParkingException("Carpark id does not belong to any carpark")

        vehicleNumber = input("Enter vehicle number: ")

        timeIn = input("Enter time in in dd/mm/yyyy hh:mm AM/PM format: ")
        date, time, AMPM = timeIn.split()
        day, month, year = date.split('/')
        hour, minute = time.split(':')

        year, month, day, hour, minute = int(year), int(month), int(day), int(hour), int(minute)

        if AMPM.upper() == 'PM':
            hour += 12

        timeIn = datetime(year, month, day, hour, minute)

        print(carparkTrackingSystem.searchCarParkById(1))

        if vehicleType == 1:
            parking = CarParking(timeIn, vehicleNumber, carparkTrackingSystem.searchCarParkById(carparkId))
            carparkTrackingSystem.addParking(parking)
        else:
            parking = MotorbikeParking(timeIn, vehicleNumber, carparkTrackingSystem.searchCarParkById(carparkId))
            carparkTrackingSystem.addParking(parking)

        print(f"{parking} *added")

    except ParkingDetailException as e:  # todo watch seminar again
        print(e)
        choice = input("Do you want to exit the vehicle for this parking? y/n: ")
        if choice[0].upper() == 'Y':
            e.parking.timeOut = timeIn
            print(f"Charges: ${e.parking.charges:.2f}")

            if vehicleType == 1:
                parking = CarParking(timeIn, vehicleNumber, carparkTrackingSystem.searchCarParkById(carparkId))
                carparkTrackingSystem.addParking(parking)
            else:
                parking = MotorbikeParking(timeIn, vehicleNumber, carparkTrackingSystem.searchCarParkById(carparkId))
                carparkTrackingSystem.addParking(parking)

            print(parking)

        else:
            print("Choosing not to exit previous parking")

    except ParkingException as e:
        print(e)

    except Exception as e:
        print(e)


def exitCarpark(carparkTrackingSystem):
    print("Exit Carpark selected")
    try:
        vehicleNumber = input("Enter vehicle number: ")
        for currentParking in carparkTrackingSystem.getParkingByVehicleNumber(vehicleNumber):
            parking = currentParking

        print(parking)

        timeOut = input("Enter time out in dd/mm/yyyy hh:mm AM/PM format: ")
        date, time, AMPM = timeOut.split()
        day, month, year = date.split('/')
        hour, minute = time.split(':')

        year, month, day, hour, minute = int(year), int(month), int(day), int(hour), int(minute)

        if AMPM.upper() == 'PM':
            hour += 12

        timeOut = datetime(year, month, day, hour, minute)

        parking.timeOut = timeOut
        print(parking)
        print(f"Charges: ${parking.charges:.2f}")

    except ParkingException as e:
        print(e)

    except Exception as e:
        print(e)

def displayParkingSummary(carparkTrackingSystem):
    print("Display Parking Summary for all Carparks selected")
    print(carparkTrackingSystem.listParkingByAllCarpark())


def main():
    carparkTrackingSystem = CarParkTrackingSystem()
    carpark1 = CarPark("11A Clementi Ave 12")
    carpark2 = CentralAreaCarPark(1.1, "123 Syed Ameen Road")
    carparkTrackingSystem.addCarpark(carpark1)
    carparkTrackingSystem.addCarpark(carpark2)

    # display of menu, getting option and decision flow
    while True:
        option = menuOption()
        if option == 0:
            break
        elif option == 1:
            parkAVehicle(carparkTrackingSystem)
        elif option == 2:
            exitCarpark(carparkTrackingSystem)
        else:
            displayParkingSummary(carparkTrackingSystem)


main()
