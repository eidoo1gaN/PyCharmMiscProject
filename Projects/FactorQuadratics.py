import numpy as np


#factor the equations that are in the form of y = ax^2 + bx + c
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

form = input("Vertex or Factored? (v/f): ")

#methods
def find_roots(A, B, C):

    i = 0
    roots_product = A*C
    roots_sum = B

    FACTOR1 = 0
    FACTOR2 = 0

    while i <= abs(roots_product):
        i += 1
        potential_factor = roots_product/i
        print("rp", roots_product)
        if potential_factor == roots_sum - i:
            FACTOR1 = potential_factor
            break
        elif -potential_factor == roots_sum - i:
            FACTOR1 = -potential_factor
            break
    print(FACTOR1)

def construct_output(factored_format, roots, vertex):
    match factored_format:
        case "v":
            pass
        case "f":
            pass
        case _:
            return "Invalid Form"


#body

find_roots(a, b, c)

