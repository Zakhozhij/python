# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
text = "abcdefabc"
find_text ="c"
n=0
for char in range (len(text)):
    str_for_search=""
    for i in range (len(find_text)):
        if char+i<len(text):
            str_for_search+=text[char+i]
    if find_text==str_for_search:
        n+=1
print(n)


     