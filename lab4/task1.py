import math

x = float(input("Введіть x: "))

f = 4 ** (2 * x) - math.log(math.cos(x)) / (
    2 - (x ** 2 + 1) ** (1 / 3)
)

print("f(x) =", f)