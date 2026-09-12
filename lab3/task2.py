import sys

n = int(sys.argv[1])

angle = (n - 2) * 180 / n

print("Кількість кутів:", n)
print("Величина внутрішнього кута:", angle, "градусів")