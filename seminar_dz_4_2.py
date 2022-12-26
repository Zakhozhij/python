#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input('Введите число N: '))
numbers_list=[]
while N!=1:
    i=2
    while N%i!=0:
        i+=1
    numbers_list.append(i)
    N/=i
print(numbers_list)