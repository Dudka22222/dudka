import math

x = float(input("Введіть x: "))

if x >= 7.2:
    f = math.log(abs(x + 1), 4)

elif x > -5.11:
    f = math.sqrt(math.log(abs(math.cos(x))))

else:
    f = x ** 2 + 4 * abs(x - 4) + math.exp(x)

print("f(x) =", f)