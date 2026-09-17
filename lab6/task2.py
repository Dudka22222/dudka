import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

x = a

while x <= b:
    y = math.log(abs(x + math.exp(x)), 3)

    print("x =", x, "f(x) =", y)

    x = x + h