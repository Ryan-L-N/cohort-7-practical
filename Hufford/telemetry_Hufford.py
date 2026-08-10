distance = input("Please select kilometers or miles:  ")
if distance == "miles":
    miles = int(input("How many miles above Mars?  "))
    if miles <= 0:
        print("You have crashed into the surface and are likely dead.")
    feet = (miles * 5280)
    yards = (miles * 1760)
    inches = (miles * 63360)
    print(f"You are {yards} yards, or {feet} feet, or {inches} inches above Mars.")
elif distance == "kilometers":
    kilometers = int(input("How many kilometers above Mars?  "))
    if kilometers <= 0:
        print("You have crashed into the surface and are likely dead.")
    meters = (kilometers * 1000)
    centimeters = (kilometers * 100000)
    millimeters = (kilometers * 1000000)
    print(f"You are {meters} meters, or {centimeters} centimeters, or {millimeters} millimeters above Mars.")
else:
    print("Please only input miles or kilometers. ")