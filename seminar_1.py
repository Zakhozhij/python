# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))

if (b == a*a or a == b*b):
    print('Yes')
else:
    print('No')