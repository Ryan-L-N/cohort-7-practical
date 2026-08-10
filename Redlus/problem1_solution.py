def miles_to_units(miles):
    return {
        "yards": miles * 1760,
        "feet": miles * 5280,
        "inches": miles * 63360,
        "kilometers": miles * 1.609344,
    }

def kilometers_to_meters(kilometers):
    return {
        "meters": kilometers * 1000,
        "centimeters": kilometers * 10000,
        "milimeters": kilometers * 100000
    }

distance_above_type = str(input("Miles above Mars (Mi) or Kilometers above Mars (Km): ")).lower()
if distance_above_type[0] == "m":
    distance_above_type = "miles"
else:
    distance_above_type = "kilometers"

distance_input = int(input(f"Enter number of {distance_above_type}: "))
if distance_above_type == "miles":
    print(miles_to_units(distance_input))

else:
    print(kilometers_to_meters(distance_input))