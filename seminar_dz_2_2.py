# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
N = int(input('Введите число: '))


def set_of_numbers(x):
    numbers_arr = []
    for i in range(1, x+1):
        numbers_arr.append(fact(i))
    return numbers_arr


def fact(a):
    if (a < 2):
        return 1
    return a*fact(a-1)


if (N > 0):
    print(set_of_numbers(N))
else:
    print("Введите число от 1 и выше")
