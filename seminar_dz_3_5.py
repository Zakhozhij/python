# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

N = int(input('Введите число: '))


def set_of_numbers(x):
    numbers_arr = []
    for i in range(-x, x+1):
        print(i)
        if (i >= 0):
            numbers_arr.append(fib(i))
        else:
            numbers_arr.append(neg_fib(i))
    return numbers_arr


def fib(x):
    return int(
        (((1+5**0.5)/2)**x - ((1-5**0.5)/2)**x)/(5**0.5)
    )


def neg_fib(x):
    return int(
        ((-1)**abs(x+1))*(((1+5**0.5)/2)**abs(x) - ((1-5**0.5)/2)**abs(x))/(5**0.5)
    )


list_of_numbers = set_of_numbers(N)
print("Current list -> ", list_of_numbers)
