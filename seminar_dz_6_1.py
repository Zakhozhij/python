#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from random import randint
A=[randint(1, 10) for _ in range(1,3)] 
B=[randint(1, 10) for _ in range(1,3)] 
print('A->',A)
print('B->',B)
result=lambda a,b:(((b[0]-a[0])**2)+((b[1]-a[1])**2))**(1/2)
print(round(result(A,B),2))