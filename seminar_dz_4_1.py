#Вычислить число c заданной точностью d
import math
a=math.pi
d = float(input('Введите точность: '))
n=0
if 10**(-10)<=d<=10**(-1):
    while d<1:
        d*=10
        n+=1
    print(round(a,n))
else:
    print("Неверно указанная точность")