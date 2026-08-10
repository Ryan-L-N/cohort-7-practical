def calculate_fuel(mass):
    return mass // 3 - 2


from pathlib import Path


def calculate_fuel(mass):
    return mass // 3 - 2


input_path = Path(__file__).with_name("input.txt")
total_fuel = 0

with input_path.open("r") as input_file:
    for line in input_file:
        if line.strip():
            mass = int(line.strip())
            total_fuel += calculate_fuel(mass)

print("Total fuel required:", total_fuel)