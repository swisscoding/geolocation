#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
from geopy.geocoders import Nominatim

# decoration
print(stylize("\n---- | Geographic conversion | ----\n", fg("red")))

# class
class GeographicConversion:
    def __init__(self, choice, locator):
        self.choice = choice
        self.locator = locator

    # methods
    def convert_into_address(self, locator):
        coordinates = input("Coordinates seperated with comma: ")
        try:
            location = locator.reverse(coordinates)
            return stylize(str(location.address) + "\n", fg("red"))
        except:
            exit("\nInvalid Coordinates\n")

    def convert_into_coordinates(self, locator):
        address = input("Address: ")
        try:
            location = locator.geocode(address)
            return stylize(str((location.latitude, location.longitude)) + "\n", fg("red"))
        except:
            exit("\nInvalid Address\n")

    # output magic method
    def __repr__(self):
        if self.choice == "a":
            return self.convert_into_address(self.locator)
        else:
            return self.convert_into_coordinates(self.locator)

# main execution
if __name__ == "__main__":
    # user interaction
    email = input("Your email address: ")
    print(stylize("\nOptions:", fg("green")))
    choice = input("'a' for coordinates into address\n\
'b' for address into coordinates\n\n: ").lower()

    # locator
    geolocator = Nominatim(user_agent=email)

    if choice != "a" and choice != "b":
        exit("\nInvalid Input\n")

    print(GeographicConversion(choice, geolocator))
