# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

N = int(input('Введите количество элементов списка: '))


def set_of_numbers(x):
    numbers_arr = []
    for i in range(0, x):
        print('Введите элемент списка ', i, ': ', end="")
        numbers_arr.append(int(input()))
    return numbers_arr


def result(numbers):
    results = 0
    for i in range(0, len(numbers)):
        if i % 2 != 0:
            print("numbers[", i, "] -> ", numbers[i])
            results += numbers[i]
    return results


print("Result -> ", result(set_of_numbers(N)))
