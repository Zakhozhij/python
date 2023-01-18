#Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)
from random import randint
import math
a=[randint(1, 10)  for _ in range(1,randint(5, 11) )]
print(a)

multiplication=lambda a,b: a*b
lits_numbers=[]
for indx,value in enumerate(a):
    if indx<math.ceil(len(a)/2):
        lits_numbers.append(multiplication(a[indx],a[len(a)-1-indx]))

print(lits_numbers)

