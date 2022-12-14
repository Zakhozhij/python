# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
day_of_week = int(input('Введите номер дня недели: '))
if day_of_week > 7 or day_of_week < 1:
    print('Вы вышли за диапазон номеров')
elif day_of_week == 6 or day_of_week == 7:
    print(day_of_week, " -> YES")
else:
    print(day_of_week, " -> NO")
