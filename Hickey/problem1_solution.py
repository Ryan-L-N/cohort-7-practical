def prob_1_telemetry():
    def miles_func():
        miles = float(input("How many miles above mars are you? "))
        feet = miles * 5280
        yards = feet / 3
        inches = feet * 12
        print(
            f"There are {yards} yards, {feet} feet, and {inches} inches in {miles} miles."
        )

    def km_func():
        km = float(input("How many km above mars are you? "))
        meters = km * 1000
        cm = meters * 100
        mm = meters * 1000
        print(f"There are {meters} meters, {cm} cm, {mm} mm in {km} km.")

    system = "pass"
    acceptable = ["mile", "miles", "kilometer", "kilometers", "km"]
    while system not in acceptable:
        system = input("Do you want miles or kilometers? ").lower()
        if system == "miles" or system == "mile":
            miles_func()
        elif system == "kilometers" or system == "kilometer" or system == "km":
            km_func()


prob_1_telemetry()
