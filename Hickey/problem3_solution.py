import math


# Problem 3
def prob3():
    def get_fuel(mass):
        return math.floor(mass / 3) - 2

    info = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            info.append(get_fuel(int(line)))
    return sum(info)


print(f"Total fuel required is: {prob3()}")
