a1 = int(input("Введіть a1: "))
a2 = int(input("Введіть a2: "))
a3 = int(input("Введіть a3: "))
N = int(input("Введіть N: "))

if N % a1 == 0 and N % a2 == 0 and N % a3 == 0:
    print("Число N є спільним кратним чисел a1, a2, a3")
else:
    print("Число N не є спільним кратним чисел a1, a2, a3")