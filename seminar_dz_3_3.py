# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# В условии задачи не сказано, что делать с нулевыми дробными частями(((((
N = int(input('Введите количество элементов списка: '))


def set_of_numbers(x):
    numbers_arr = []
    for i in range(0, x):
        print('Введите элемент списка ', i, ': ', end="")
        a = float(input())
        numbers_arr.append(round(a-int(a), 2))
    return numbers_arr


def get_max(numbers):
    max = 0
    if len(numbers) > 0:
        max = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max and numbers[i] != 0:
            max = numbers[i]
    return max


def get_min(numbers):
    min = 0
    if len(numbers) > 0:
        min = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min and numbers[i] != 0:
            min = numbers[i]
    return min


list_of_numbers = set_of_numbers(N)
print("List without int -> ", list_of_numbers)
print("Result -> ", get_max(list_of_numbers)-get_min(list_of_numbers))
