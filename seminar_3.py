#Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
X = input('Введите строку: ')
N = int(input('Введите количество элементов списка: '))


def set_of_numbers(x):
    numbers_arr = []
    for i in range(0, x):
        print('Введите элемент списка ', i, ': ', end="")
        numbers_arr.append(str(input()))
    return numbers_arr

def find_X(array_list,x):
    n=0
    for i in range(0, len(array_list)):
        a=array_list[i].find(x)
        if a!=-1 and n==0:
            n+=1
        elif a!=-1 and n==1:
            return i
    return 0

list_of_numbers = set_of_numbers(N)
print("List -> ", list_of_numbers)
print(find_X(list_of_numbers,X))
