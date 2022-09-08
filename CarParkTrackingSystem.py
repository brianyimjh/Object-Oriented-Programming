from ParkingDetailException import ParkingDetailException


class CarParkTrackingSystem:  # todo replace the old one with this

    def __init__(self, carparks=None, parkings=None):
        """ constructor that execute when an object is created """
        # carpark = [Carpark object]
        # parking = [Parking object]

        if carparks is None:
            self._carparks = []
        else:
            self._carparks = carparks

        if parkings is None:
            self._parkings = []
        else:
            self._parkings = parkings

    def searchCarParkById(self, carparkId):
        for carpark in range(len(self._carparks)):
            if self._carparks[carpark].carparkId == carparkId:
                return self._carparks[carpark]
        return None

    def searchCarParkByAddress(self, address):
        for carpark in range(len(self._carparks)):
            if self._carparks[carpark].address == address:
                return self._carparks[carpark]
        return None

    def addCarpark(self, carpark):
        """ The method searches the collection of carparks by address, and if
        the carpark with the address is not in the collection yet, then the carpark is
        added, and the method returns True. Otherwise, the method returns False.
        """
        if self.searchCarParkByAddress(carpark.address) is None:
            self._carparks.append(carpark)
            return True
        return False

    def getParkingByVehicleNumber(self, vehicleNumber, currentOnly=True):
        """ If currentOnly is False, the method returns a list of all parking for a given parameter value,
        vehicleNumber. If currentlyOnly is True, the method returns a list of all parking for vehicleNumber still in
        a carpark. """
        currentParking = []
        allParking = []

        for parking in range(len(self._parkings)):
            if self._parkings[parking].vehicleNumber == vehicleNumber:
                if self._parkings[parking].timeOut is None:
                    currentParking.append(self._parkings[parking])
                allParking.append(self._parkings[parking])

        if not currentOnly:
            return allParking
        else:
            return currentParking

    def getParkingByCarpark(self, carparkId, currentOnly=True):
        """ If currentOnly is False, the method returns a list of
        parking for a carpark with the parameter carparkId. If currentlyOnly is True, the
        method returns a list of parking for vehicles still in the carpark.
        """
        currentParking = []
        allParking = []

        for parking in range(len(self._parkings)):
            if self._parkings[parking].carpark.carparkId == carparkId:
                if self._parkings[parking].timeOut is None:
                    currentParking.append(self._parkings[parking])
                allParking.append(self._parkings[parking])

        if not currentOnly:
            return allParking
        else:
            return currentParking

    def addParking(self, parking):  #todo watch seminar again
        """ The method adds the parameter parking to the list of parking if the
        vehicle has already left the carpark for all its previous parking """
        if not self.getParkingByVehicleNumber(parking.vehicleNumber):  # if first parking, simply append parking
            self._parkings.append(parking)
            return True

        else:
            for currentParking in self.getParkingByVehicleNumber(parking.vehicleNumber):
                if currentParking.timeOut is None:
                    raise ParkingDetailException("Error in adding a parking. Parking record shows vehicle is still in a "
                                                 "carpark.", currentParking)
                else:
                    self._parkings.append(parking)
                    return True

    def listParkingByAllCarpark(self):
        """ The method returns a string consisting of details of
        parking in each carpark, a summarised detail of the total collected and the
        number of vehicles that are still in the carparks """
        totalAmount = 0.00
        totalVehiclesParked = 0
        summaryText = ""

        for carpark in range(len(self._carparks)):
            text = ""
            carparkCharges = 0.00
            completedParking = 0
            carparkId = self._carparks[carpark].carparkId
            vehiclesParked = len(self.getParkingByCarpark(carparkId))

            text += f"Detail of {self._carparks[carpark].__str__()}\n"

            for parking in range(len(self.getParkingByCarpark(carparkId, False))):
                text += f"{self.getParkingByCarpark(carparkId, False)[parking].__str__()}\n"
                if self.getParkingByCarpark(carparkId, False)[parking].timeOut is None:
                    carparkCharges += 0.00
                else:
                    completedParking += 1
                    carparkCharges += self.getParkingByCarpark(carparkId, False)[parking].charges

            totalAmount += carparkCharges
            text += f"Number of completed parking: {completedParking}\nNumber of vehicles parked in carpark currently: {vehiclesParked}\nTotal amount: ${carparkCharges:.2f}\n\n"

            summaryText += text
            totalVehiclesParked += vehiclesParked

        summaryText += f"Summary for all carparks\nTotal collected: ${totalAmount:.2f}\nNumber of vehicles parked in all carparks currently: {totalVehiclesParked}"

        return summaryText
