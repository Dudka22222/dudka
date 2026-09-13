import math


def calculate_z(x, y, m):
    z = (
        math.sqrt(x ** 3 + math.pi ** 2)
        + math.exp(y + 1)
        + m ** (1 / 3)
        + math.tan(m)
    )
    return z


x = float(input("Введіть x: "))
y = float(input("Введіть y: "))
m = float(input("Введіть m: "))

z = calculate_z(x, y, m)

print("Z =", z)