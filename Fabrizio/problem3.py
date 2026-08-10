# Problem 3 - Rocket Fuel Calculation


def fuel_required(mass: int) -> int:
    return (mass // 3) - 2


def total_fuel(inputfile: str) -> int:
    total = 0

    with open(inputfile, "r") as f:
        for line in f:
            line = line.strip()

            if line:
                mass = int(line)
                fuel = fuel_required(mass)
                total += fuel

    return total


answer = total_fuel("input.txt")
print(f"Total fuel required: {answer}")
