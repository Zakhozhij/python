#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
numbers='1111111111111112222334445'
letters='AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'


def rle_algoritm(str_text):
    result=[]
    num=0
    start_step=0
    while start_step<len(str_text):
        for j in range(start_step,len(str_text)):
            if str_text[j]==str_text[start_step]:
                num+=1
                if j==len(str_text)-1:
                    result.append([str(num),str(str_text[j])])
                    start_step=len(str_text)
                    break
            else:
                result.append([str(num),str(str_text[start_step])])
                start_step=j
                num=0
                break


    return result

def restore_rle_algoritm(list):
    result=''
    for i in list:
        result+=int(i[0])*i[1]
    return result

def convert_to_string(list):
    result=''
    for i in list:
        result+=str(i[0])+str(i[1])
    return result

print(numbers)
print(letters)
print('------------------------')
print('Алгоритм сжатия')
result_list_numbers=rle_algoritm(numbers)
result_list_letters=rle_algoritm(letters)

print(convert_to_string(result_list_numbers))
print(convert_to_string(result_list_letters))
print('------------------------')
print('Алгоритм восстановления')
print(restore_rle_algoritm(result_list_numbers))
print(restore_rle_algoritm(result_list_letters))