with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
totalweight = sum(map(int, lines))
print(f"The total weight of the load is {totalweight}.")
fuelneeded = (totalweight // 3) - 2
print(f"The fuel needed to for {totalweight} mass is {fuelneeded}.")