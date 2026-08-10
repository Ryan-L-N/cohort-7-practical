# Chief Engineer — you're receiving this message because you ranked top in systems diagnostics during pre-deployment training. We need that expertise now. Three sols ago, an unexpected solar flare—classified X9.3—hit the upper atmosphere, causing a cascading failure in Base One’s remote operations stack. Our telemetry systems, environmental monitors, and autonomous rover schedulers all went dark.
# We’ve managed to bring emergency power online, but mission control remains offline. We have less than 72 hours before the incoming resupply and colonist wave lands. If core systems aren’t restored, we can expect to lose all 1000 people on board. Your assignment is clear: 


# Gain remote access of Mission Control (log in to the VM), cd into the /home/engineer directory, and run the final_project.py script. It will perform a series of diagnostics and attempt to restore critical systems. You must identify and fix any issues in the code to ensure the script runs successfully. Time is of the essence—failure is not an option.
import math


def circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2


def equilateral_triangle_area(side):
    return (math.sqrt(3) / 4) * side ** 2


def square_area(side):
    return side ** 2


# Automatron 1: two circular pizzas, 15-inch diameter
automatron_1_area = 2 * circle_area(15)
automatron_1_efficiency = automatron_1_area / 20

# Automatron 2: one equilateral triangle, side length 20
automatron_2_area = equilateral_triangle_area(20)
automatron_2_efficiency = automatron_2_area / 20

# Automatron 3: one square, side length 18
automatron_3_area = square_area(18)
automatron_3_efficiency = automatron_3_area / 18

efficiencies = {
    "Automatron 1": automatron_1_efficiency,
    "Automatron 2": automatron_2_efficiency,
    "Automatron 3": automatron_3_efficiency,
}

print(f"Automatron 1 total area: {automatron_1_area:.2f} square inches")
print(f"Automatron 1 efficiency: {automatron_1_efficiency:.2f} square inches per dough unit")

print(f"\nAutomatron 2 total area: {automatron_2_area:.2f} square inches")
print(f"Automatron 2 efficiency: {automatron_2_efficiency:.2f} square inches per dough unit")

print(f"\nAutomatron 3 total area: {automatron_3_area:.2f} square inches")
print(f"Automatron 3 efficiency: {automatron_3_efficiency:.2f} square inches per dough unit")

best_automatron = max(efficiencies, key=efficiencies.get)

print(f"\nBest deal: {best_automatron}")