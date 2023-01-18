#Найти сумму чисел списка стоящих на нечетной позиции
from random import randint
a=[randint(1, 10)  for _ in range(1,randint(5, 11) )]
print(a)
summ=0
for indx,value in enumerate(a):
    if indx%2==1:
        summ+=value
print(summ)