# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
x1 = int(input('Введите число x1: '))
y1 = int(input('Введите число y1: '))

x2 = int(input('Введите число x2: '))
y2 = int(input('Введите число y2: '))

print('A (', x1, ',', y1, '); B (', x2, ',', y2, ') ->',
      round((((x2-x1)**2 + (y2-y1)**2)**(0.5)), 2))
