# Cohort 7 Small Project (Garcia)

### Remote Access ###

# Imports I thought I was going to need
import requests
from requests.auth import HTTPBasicAuth
import os

# This part was done in the terminal
# curl.exe # curl.exe 20.127.202.175:8000
# X-Username = "chief.engineer"
# X-Password = "ares-vallis-7"
# curl.exe -H "X-Username: chief.engineer" -H "X-Password: ares-vallis-7" 20.127.202.175:8000

# username = 'chief.tech'
# password = '1000-souls-aboard
# ssh chief.tech@20.127.202.175


### Python Problem 1 ###

# As the colonists approach Mars, you need to help them calculate their telemetry data.
# To do this, you are going to write a python program.
# The program should ask the user if they would like to input either "Miles above Mars" or "Kilometers above Mars".

# If they choose "Miles above Mars", the program should then prompt them to enter the number of miles.
# Then the program should display the number of yards, feet, and inches that are in that many miles.
# If the user chooses "Kilometers above Mars", the program should then prompt them to enter the number of kilometers.
# Then the program should display the number of meters, centimeters, and millimeters that are in that many kilometers.


# Start with function definitions for calculations to be used after
def convert_miles(miles):
    yards = miles * 1760
    feet = miles * 5280
    inches = miles * 63360

    # Display results
    print(f"{miles} miles is equal to:")
    print(f"{yards} yards")
    print(f"{feet} feet")
    print(f"{inches} inches")


def convert_km(kilometers):
    meters = kilometers * 1000
    centimeters = meters * 100
    millimeters = centimeters * 10

    # Display results
    print(f"{kilometers} kilometers is equal to:")
    print(f"{meters} meters")
    print(f"{centimeters} centimeters")
    print(f"{millimeters} millimeters")


# Ask user to choose unit of measure
unit_choice = input(
    'Please specify either "Miles above Mars" or "Kilometers above Mars" '
)

# Figure out unit conversions
if "mi" in unit_choice.lower():
    distance_input = int(input("Please enter the number of miles: "))
    convert_miles(distance_input)
elif "kilometer" in unit_choice.lower() or "km" in unit_choice.lower():
    distance_input = int(input("Please enter the number of kilometers: "))
    convert_km(distance_input)
else:
    print("Erroneous input. Please try again.")


### Python Problem 2 ###
import math


# Area functions
def circ_area(diameter: float) -> float:
    area = 0.25 * diameter**2
    return area


def tri_area(side: float) -> float:
    area = (math.sqrt(3) / 4) * side**2
    return area


def sq_area(side: float) -> float:
    area = side**2
    return area


# Each pizza automaton area per dough unit
auto1_pizza = (circ_area(15) * 2) / 20
auto2_pizza = tri_area(20) / 20
auto3_pizza = sq_area(18) / 18

# Print Results
print()
print("Choose the automaton with the highest dough efficiency:")
print(f"1st Automatron: {auto1_pizza:.3f}")
print(f"2nd Automatron: {auto2_pizza:.3f}")
print(f"3rd Automatron: {auto3_pizza:.3f}")
print()


### Problem 3 ###

# Read a file with each line representing mass
with open("input.txt", "r") as file:
    masses = [line.rstrip("\n") for line in file]


# Mass formula
def fuel_mass(mass: float) -> float:
    fuel = math.floor(mass / 3) - 2
    return fuel


# Calculate total fuel needed
total_fuel = 0
for mass in masses:
    total_fuel += fuel_mass(int(mass))

# Display results
print(f"Total fuel requirements of all modules: {total_fuel}\n")
