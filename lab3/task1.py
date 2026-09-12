a = int(input("Введіть перше тризначне число: "))
b = int(input("Введіть друге тризначне число: "))

last_a = abs(a) % 10
last_b = abs(b) % 10

sum_digits = last_a + last_b
product_digits = last_a * last_b

print("Остання цифра першого числа:", last_a)
print("Остання цифра другого числа:", last_b)
print("Сума останніх цифр:", sum_digits)
print("Добуток останніх цифр:", product_digits)