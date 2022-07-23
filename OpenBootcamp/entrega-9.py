from math import pi


def area_triangulo(base, altura):
    return (base*altura)/2

def area_ciruclo(radio):
    return pi*radio**2


print(area_triangulo(24,4))
print(area_ciruclo(3))