# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
N = int(input('Введите число: '))


def get_new_number(a):
    if a == 1:
        return 1
    if a % 2 == 0:
        b = 0
    else:
        b = 1

    return str(b)+str(get_new_number(int(a/2)))


print(get_new_number(N)[::-1])
