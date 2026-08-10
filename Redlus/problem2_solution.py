# The first Automatron produces 2 circular pizzas (15 inch diameter) that require 20 units of dough.
# The second Automatron makes a larger, equilateral triangle pizza, side length 20, that also requires 20 units of dough.
# The third Automatron creates a square pizza with side length 18, that only requires 18 units of dough.

# As the Chief Engineer, you decide to write a Python Script to figure out which Automatron is most efficient.  Once we avert total di>
# we will want to welcome them with some warm, Martian pizza after all.

def area_calc_round(x, res):
    return (((3.14 * (float(x)/2) ** 2)*2) / res)

def area_calc_sq(x, res):
    return ((x * x) / res)

def area_calc_tri(x, res):
    return (((3 ** 0.5 / 4) * x ** 2) / res)

print(f"First automataton: {area_calc_round(15, 20)}")
print(f"Second automataton: {area_calc_tri(20, 20)}")
print(f"Third automataton: {area_calc_sq(18, 18)}")