#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.'
import random
k = int(input('Введите натуральную степень k: '))

def get_equation(x):
    result=''
    while x>0:
        if x>1:
            result+=str(random.randint(0, 101))+"x**"+str(x)+"+"
        else:
            result+=str(random.randint(0, 101))+"x+"+str(random.randint(0, 101))+"=0"
        x-=1
    return result
print("k -> ",k)
stroke=get_equation(k)
print(stroke)
with open("file.txt", "w") as f:
    f.write(stroke)