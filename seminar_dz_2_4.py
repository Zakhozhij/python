# Реализуйте алгоритм перемешивания списка.
import random
N = int(input('Введите количество элементов списка: '))


def set_of_numbers(x):
    numbers_arr = []
    for i in range(1, x+1):
        print('Введите элемент списка ', i, ': ', end="")
        numbers_arr.append(int(input()))
    return random.sample(numbers_arr, len(numbers_arr))


if (N > 0):
    print(set_of_numbers(N))
else:
    print("Введите число от 1 и выше")
