# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

N = int(input('Введите количество элементов списка: '))


def set_of_numbers(x):
    numbers_arr = []
    for i in range(0, x):
        print('Введите элемент списка ', i, ': ', end="")
        numbers_arr.append(int(input()))
    return numbers_arr


def result(numbers):
    results = []
    for i in range(0, len(numbers)):
        if numbers[i] and i < len(numbers)/2:
            results.append(numbers[i]*numbers[len(numbers)-i-1])
    return results


list_of_numbers = set_of_numbers(N)
print("Current list -> ", list_of_numbers)
print("Result list -> ", result(list_of_numbers))
