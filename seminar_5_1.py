#Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda. 
#[1, 2, 3, 5, 7, 8, 9, 10] 
#[1, 2, 4, 8, 9]

a=[1, 2, 3, 5, 7, 8, 9, 10] 
b=[1, 2, 4, 8, 9]
cancat=list(filter((lambda x: x in a),b))

print(cancat)