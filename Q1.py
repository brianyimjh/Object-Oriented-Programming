class Newspaper:
    # Class variable for online rate
    _RATE_PER_MONTH_ONLINE = 0.5

    def __init__(self, name, language, ratePerMonthPrint):
        """ constructor that execute when an object is created """
        self._name = name
        self._language = language
        self._ratePerMonthPrint = ratePerMonthPrint

    @property
    def name(self):
        return self._name

    @property
    def language(self):
        return self._language

    @property
    def ratePerMonthPrint(self):
        return self._ratePerMonthPrint

    @ratePerMonthPrint.setter
    def ratePerMonthPrint(self, ratePerMonthPrint):
        self._ratePerMonthPrint = ratePerMonthPrint

    def ratePerMonthOnline(self):
        """ The method returns the monthly subscription rate for an
        online version of the newspaper which is 50% the rate for a printed version. """
        # Using class variable to calculate
        return self._ratePerMonthPrint * type(self)._RATE_PER_MONTH_ONLINE

    def __str__(self):
        """ return the string representation of the object """
        return f"Name: {self._name}\tLanguage: {self._language}\tCurrent Rate Print: ${self._ratePerMonthPrint:.2f}/mth\tOnline: ${self.ratePerMonthOnline():.2f}/mth"


def Q1a():
    # Part (ii)
    n1 = Newspaper("Today's News", "English", 34.90)
    n2 = Newspaper("Berita Hari", "Malay", 45.90)
    n3 = Newspaper("Zao Pao", "Chinese", 47.50)
    n4 = Newspaper("Inru ceyti", "Tamil", 47.90)

    # Part (iii)
    n1.ratePerMonthPrint += 5
    print(f"New rate of Today's News: ${n1.ratePerMonthPrint:.2f}")

    # Part (iv)
    print(f"Name of the second newspaper: {n2.name}")
    print(f"Language of the second newspaper: {n2.language}")
    print(f"Details of the third newspaper -\n{n3}")


class Subscription:

    def __init__(self, name, address, contact, newspaper, printedVersion=True):
        """ constructor that execute when an object is created """
        self._name = name
        self._address = address
        self._contact = contact
        self._newspaper = newspaper
        self._printedVersion = printedVersion
        if printedVersion:
            self._ratePerMonth = newspaper.ratePerMonthPrint
        else:
            self._ratePerMonth = newspaper.ratePerMonthOnline()

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @property
    def contact(self):
        return self._contact

    @property
    def newspaper(self):
        return self._newspaper

    @property
    def printedVersion(self):
        return self._printedVersion

    @property
    def ratePerMonth(self):
        return self._ratePerMonth

    @contact.setter
    def contact(self, contact):
        self._contact = contact

    def newspaperName(self):
        return self._newspaper.name

    def changeVersion(self):
        """ The method changes the newspaper version that the subscription
        is for. Rate per month is adjusted accordingly, based on the prevailing subscription rate for the newspaper. """
        if self._printedVersion == True:
            self._printVersion = False
            self._ratePerMonth = self._newspaper.ratePerMonthOnline()
        elif self._printedVersion == False:
            self._printVersion = True
            self._ratePerMonth = self._newspaper.ratePerMonthPrint

    def __str__(self):
        """ return the string representation of the object """
        return f"{self._name} {self._address} {self._contact} Print version: {'Yes' if self._printedVersion == True else 'No'} Subscription Rate: ${self._ratePerMonth:.2f} per month\n{self._newspaper.__str__()}"


def Q1b():
    # Part (ii)
    n1 = Newspaper("Today's News", "English", 34.90)
    sub1 = Subscription("Peter", "42 Simei Drive", 96667878, n1, False)
    sub2 = Subscription("John", "12 Clementi Road", 98769876, n1)

    # Part (iii)
    print(sub1)
    print(f"Subscription 2 newspaper name: {sub2.newspaperName()}")

    # Part (iv)
    n1.ratePerMonthPrint = 37.50
    sub1.changeVersion()

    # Part (v)
    print(f"Subscription 1 monthly rate: ${sub1.ratePerMonth:.2f}")
    print(f"Subscription 2 monthly rate: ${sub2.ratePerMonth:.2f}")

    print(f"Current newspaper rate (printed): ${n1.ratePerMonthPrint:.2f}")
    print(f"Current newspaper rate (online): ${n1.ratePerMonthOnline():.2f}")


class Publisher:

    def __init__(self, newspaperList=None):
        """ constructor that execute when an object is created """
        if newspaperList is None:
            self._newspaperList = {}
        else:
            self._newspaperList = newspaperList

    def searchNewspaper(self, name):
        """ The method returns a newspaper in _newspaperList with a
        name that matches the parameter name. The method returns None otherwise. """
        return self._newspaperList.get(name, None)

    def addNewspaper(self, name, newspaper):
        """ The method adds a newspaper to _newspaperList. """
        if self.searchNewspaper(name) is None:
            self._newspaperList[name] = newspaper

    def changeNewspaperRate(self, name, newRate):
        """ The method searches for a newspaper in
        _newspaperList that has the same name as the parameter name, and changes the subscription rate for that newspaper. The method returns True if the search is successful and the change is made, Otherwise, the method returns False. """
        if self.searchNewspaper(name) is not None:
            self._newspaperList[name].ratePerMonthPrint = newRate
            return True
        else:
            return False

    def __str__(self):
        """ return the string representation of the object """
        text = ""
        for newspaper in self._newspaperList.values():
            text += f"{newspaper.__str__()}\n"

        return text


def Q1c():
    # Part (ii)
    n1 = Newspaper("Today's News", "English", 34.90)
    n2 = Newspaper("Berita Hari", "Malay", 45.90)
    n3 = Newspaper("Zao Pao", "Chinese", 47.50)
    n4 = Newspaper("Inru ceyti", "Tamil", 47.90)
    publisher = Publisher()
    publisher.addNewspaper("Today's News", n1)
    publisher.addNewspaper("Berita Hari", n2)
    publisher.addNewspaper("Zao Pao", n3)
    publisher.addNewspaper("Inru ceyti", n4)

    # Part (iii)
    if publisher.searchNewspaper("Zao Pao") is not None:
        newspaper = publisher.searchNewspaper("Zao Pao")
        print(f"Zao Pao newspaper rate (printed): ${newspaper.ratePerMonthPrint:.2f}")
        print(f"Zao Pao newspaper rate (online): ${newspaper.ratePerMonthOnline():.2f}")
    else:
        print("Newspaper not found")

    # Part (iv)
    publisher.changeNewspaperRate("Inru ceyti", 46.50)
    print(publisher)


def main():
    Q1a()
    # Question output separator
    print("===")
    Q1b()
    # Question output separator
    print("===")
    Q1c()

main()