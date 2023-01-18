# 38)Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100
# Имеется список имен сотрудников из 10 элементов
# Сопоставьте каждому имени сотрудника его id, и выведите получившийся список.
# Выведете имена сотрудников, получившие нечетное id. Решить с помощью zip,filter,lambda
from random import randint
id=[randint(1, 101) for _ in range(10)] 
names = ['Леша1','Леша2','Леша3','Леша4','Леша5','Леша6','Леша7','Леша8','Леша9','Леша10']
employes=list(zip(id,names))
print(employes)
result=list(filter((lambda x: True if x[0]%2 != 0 else False),employes))
print([i[1] for i in result])
