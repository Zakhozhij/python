#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число: '))


def set_of_numbers(x):
    numbers_arr = []
    if x<0:
        x=abs(x)
    for i in range(-x, x+1):
        numbers_arr.append(i)
    return numbers_arr

def positions_of_numbers(x):
    positions_arr = []
    file1 = open('file.txt',"r")
    content=file1.readlines()
    for line in content:
        line=line.strip()
        if line.isdigit():
            positions_arr.append(int(line))
    file1.close()
    return positions_arr


def result(numbers,positions):
    results=1
    for i in positions: 
        if i<len(numbers):
            print("numbers[",i,"] -> ",numbers[i])
            results*=numbers[i]
    return results
print("Current list -> ",set_of_numbers(N))
print("Positions -> ",positions_of_numbers(N))

print("Result -> ",result(set_of_numbers(N),positions_of_numbers(N)))



