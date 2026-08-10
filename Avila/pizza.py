import math
#Pizza 1 Automation 2 15 inch pizza 


def two_circular_pizzas():
    diameter = 15
    radius = diameter /2
    area = math.pi * radius ** 2
    total_area = area * 2
    dough = 20
    efficiency = total_area / dough
    return efficiency 

def equilateral_triangle_pizza():
    side = 20
    area = (math.sqrt(3) / 4) * side ** 2
    dough = 20
    efficiency = area / dough
    return efficiency

def square_pizza():
    side = 18
    area = side * side
    dough = 18
    efficiency = area / dough
    return efficiency

print(" ==== Pizza Options ==== ")
print(f"Two circular pizzas: {two_circular_pizzas():.2f}")
print(f"Equilateral triangle pizza: {equilateral_triangle_pizza():.2f}")
print(f"Square pizza: {square_pizza():.2f}")

if two_circular_pizzas > equilateral_triangle_pizza and two_circular_pizzas > square_pizza:
    print("Automatron 1 is the best deal!")
elif equilateral_triangle_pizza > two_circular_pizzas and equilateral_triangle_pizza > two_circular_pizzas:
    print("Automatron 2 is the best deal!")
else:
    print("Automatron 3 is the best deal!")
    