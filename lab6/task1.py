import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

n = int((b - a) / h) + 1

for i in range(n):
    x = a + i * h
    y = math.log(abs(x + math.exp(x)), 3)

    print("x =", x, "f(x) =", y)