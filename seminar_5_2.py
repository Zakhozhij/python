#Сделать с помощью filter, lambda 
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Вывести все пробелы и их индексы из предыдущей строки.

str = 'фбв вйвац ббвфбв вуасмывбффба фбаб абв вбвабв'
lst=str.split()

lst2 =' '.join(list(filter((lambda x: 'абв' not in x.lower()),lst)))
print(lst2)
for indx,value in enumerate(str):
    if value == ' ':
        print(indx)