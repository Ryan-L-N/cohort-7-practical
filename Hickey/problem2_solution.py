import math


def prob_2_resources():
    def aut1():
        num_pies = 2
        radius = 15 / 2
        dough = 20
        area = math.pi * radius**2
        return num_pies * area / dough

    def aut2():
        side = 20
        area = side**2 / 2
        dough = 20
        return area / dough

    def aut3():
        side = 18
        dough = 18
        area = side**2
        return area / dough

    print(aut1())
    print(aut2())
    print(aut3())
    holder = []
    holder.append(aut1())
    holder.append(aut2())
    holder.append(aut3())
    winner = holder.index(max(holder)) + 1
    print(f"Aut {winner} is the winner")


prob_2_resources()
