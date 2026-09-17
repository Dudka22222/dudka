import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

values = []

x = a

while x <= b:
    y = math.log(abs(x + math.exp(x)), 3)

    values.append(y)

    x = x + h

print("Значення функції:")

for y in values:
    print(y)

average = sum(values) / len(values)

print("Середнє арифметичне =", average)