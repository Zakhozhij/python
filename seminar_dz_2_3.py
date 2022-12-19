# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
N = int(input('Введите число: '))


def set_of_numbers(x):
    numbers_arr = []
    for i in range(1, x+1):
        numbers_arr.append(get_formula(i))
    return numbers_arr


def get_formula(a):
    return round((1+1/a)**a, 2)


if (N > 0):
    print(set_of_numbers(N))
    print(sum(set_of_numbers(N)))
else:
    print("Введите число от 1 и выше")
