#Automaton 1 makes two 15 inch pizzas with 20 units of dough
#Automaton 2 makes a larger equilateral triangle pizza (Who makes a triangle Pizza???) side length 20, that also uses 20 units of dough
#Automaton 3 makes a square pizza with side length 18 that requires 18 units of dough.
import math
def Automaton1(pizzas, diameter, dough):
    auto1 = float((3.14*(diameter/2*2))*pizzas)
    auto1effic = auto1 / dough
    return auto1effic
def Automaton2(side, dough):
    auto2 = float((math.sqrt(3) / 4) * (side**2))
    auto2effic = auto2 / dough
    return auto2effic
def Automaton3(side, dough):
    auto3 = float((side**2))
    auto3effic = auto3 / dough
    return auto3effic
bot1 = Automaton1(2,15,20)
bot2 = Automaton2(20, 20)
bot3 = Automaton3(18, 18)
print(f"Automaton 1 produces {bot1} inches of pizza per unit of dough.")
print(f"Automaton 2 produces {bot2} inches of pizza per unit of dough.")
print(f"Automaton 3 produces {bot3} inches of pizza per unit of dough")
best = 0
bestname = "Hello"
if bot1 > bot2:
    best = bot1
    bestname = "Automaton 1"
elif bot2 > bot3:
    best = bot2
    bestname = "Automaton 2"
else:
    best = bot3
    bestname = "Automaton 3"
print(f"The most efficient Automaton is {bestname} which produces {best} inches of pizza per dough.")