#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
N = int(input('Введите количество элементов списка: '))

def set_of_numbers(x):
    numbers_arr = []
    for i in range(0, x):
        print('Введите элемент списка ', i, ': ', end="")
        numbers_arr.append(int(input()))
    return numbers_arr


def unik_list(numbers):
    results = []

    for i in range(0, len(numbers)):
        n=0
        for k in range(0, len(numbers)):
            if numbers[k]==numbers[i]:
                n+=1
        if n==1:
            results.append(numbers[i])
    return results


list_of_numbers = set_of_numbers(N)
print("Current list -> ", list_of_numbers)
print("Result list -> ", unik_list(list_of_numbers))
