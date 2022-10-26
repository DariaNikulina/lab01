a = int(input(" a = "))
b = int(input(" b = "))

while (a != b):
    if (a > b):
        a = a - b
    if (a < b):
        b = b - a

print(" НОД = ", a)