choice = input(
    'Enter "Miles above Mars" or "Kilometers above Mars": '
).strip().lower()

if choice == "miles above mars":
    miles = float(input("Enter the number of miles: "))

    yards = miles * 1760
    feet = miles * 5280
    inches = miles * 63360

    print("Yards:", yards)
    print("Feet:", feet)
    print("Inches:", inches)

elif choice == "kilometers above mars":
    kilometers = float(input("Enter the number of kilometers: "))

    meters = kilometers * 1000
    centimeters = kilometers * 100000
    millimeters = kilometers * 1000000

    print("Meters:", meters)
    print("Centimeters:", centimeters)
    print("Millimeters:", millimeters)

else:
    print('Invalid selection. Enter "Miles above Mars" or "Kilometers above Mars".')