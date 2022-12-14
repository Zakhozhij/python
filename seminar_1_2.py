# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
a1 = int(input('Введите число 1: '))
a2 = int(input('Введите число 2: '))
a3 = int(input('Введите число 3: '))
a4 = int(input('Введите число 4: '))
a5 = int(input('Введите число 5: '))
max = a1
if a2 > max:
    max = a2
if a3 > max:
    max = a3
if a4 > max:
    max = a4
if a5 > max:
    max = a5
print(max)
