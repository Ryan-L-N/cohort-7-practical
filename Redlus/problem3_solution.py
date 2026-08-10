# Fuel required to launch a given module is based on its mass.
# Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.

# As the Chief Engineer, you need to calculate the total fuel requirement.
# To find the total fuel requirement, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?
running_total_fuel = 0

def req_fuel(x):
    needed = (round((x / 3),0) - 2)
    return needed

number_list = []
with open('input.txt',"r") as f:
    numbers = f.readlines()
    for i in numbers:
        
        current_num = int(i)
        needed = req_fuel(current_num)
        running_total_fuel += needed
        print(f"{current_num} mass requires {needed}")
        # number_list.append(current_num)

print(f"Total Fuel needed: {running_total_fuel}")