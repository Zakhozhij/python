# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
N = float(input('Введите число: '))


def count_numbers(x):
    result = 0
    x_str = list(str(x))
    for i in x_str:
        if i.isdigit():
            result += int(i)
    return result


print(count_numbers(N))
