# Problem 2 - Food Resource Calculation

import math


def circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius**2


def equilateral_triangle_area(side):
    return (math.sqrt(3) / 4) * side**2


def square_area(side):
    return side**2


# Automatron 1: two circular pizzas, 15-inch diameter
automatron_1_area = 2 * circle_area(15)
automatron_1_efficiency = automatron_1_area / 20

# Automatron 2: one equilateral triangle, 20-inch sides
automatron_2_area = equilateral_triangle_area(20)
automatron_2_efficiency = automatron_2_area / 20

# Automatron 3: one square, 18-inch sides
automatron_3_area = square_area(18)
automatron_3_efficiency = automatron_3_area / 18

efficiencies = {
    "Automatron 1": automatron_1_efficiency,
    "Automatron 2": automatron_2_efficiency,
    "Automatron 3": automatron_3_efficiency,
}

print(f"Automatron 1 total area: {automatron_1_area:.2f} square inches")
print(
    f"Automatron 1 efficiency: "
    f"{automatron_1_efficiency:.2f} square inches per dough unit"
)

print(f"\nAutomatron 2 total area: {automatron_2_area:.2f} square inches")
print(
    f"Automatron 2 efficiency: "
    f"{automatron_2_efficiency:.2f} square inches per dough unit"
)

print(f"\nAutomatron 3 total area: {automatron_3_area:.2f} square inches")
print(
    f"Automatron 3 efficiency: "
    f"{automatron_3_efficiency:.2f} square inches per dough unit"
)

best_automatron = max(efficiencies, key=efficiencies.get)

print(f"\nBest deal: {best_automatron}")
