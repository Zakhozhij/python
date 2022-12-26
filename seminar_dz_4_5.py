#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def get_file_content(x):
    
    file_path="file_"+x+'.txt'
    file = open(file_path,"r")
    content=file.readline()
    content=content[:-2].split('+')
    file.close()
    return content
def find_max_degree(ex_list):
    return len(ex_list)-1

def result(ex_list_1,ex_list_2):  
    file_content = []
    indexes_to_remove = []
    result_str=""
    for i in range(0, len(ex_list_1)):
        for j in range(0, len(ex_list_2)):
            if '**' in ex_list_1[i] and '**' in ex_list_2[j] and ex_list_1[i].split('x**')[1]==ex_list_2[j].split('x**')[1]:
                file_content.append(str(int(ex_list_1[i].split('x**')[0])+int(ex_list_2[j].split('x**')[0]))+"x**"+ex_list_1[i].split('x**')[1])
                indexes_to_remove.append(i)
            elif '**' not in ex_list_1[i] and '**' not in ex_list_2[j] and 'x' in ex_list_1[i] and 'x' in ex_list_2[j]:
                file_content.append(str(int(ex_list_1[i].split('x')[0])+int(ex_list_2[j].split('x')[0]))+"x")
                indexes_to_remove.append(i)
            elif '**' not in ex_list_1[i] and '**' not in ex_list_2[j] and 'x' not in ex_list_1[i] and 'x' not in ex_list_2[j]:
                file_content.append(str(int(ex_list_1[i].split('x')[0])+int(ex_list_2[j].split('x')[0])))
                indexes_to_remove.append(i)
    if len(ex_list_1)>len(file_content):
        for i in range(0, len(ex_list_1)):
            if i not in indexes_to_remove:
                file_content.insert(0, ex_list_1[i])
    for i in range(0, len(file_content)):
        result_str+=file_content[i]+"+"
    return result_str[:-1]+"=0"


ex_list_1=get_file_content('1')
ex_list_2=get_file_content('2')
print(ex_list_1)
print(ex_list_2)
ex_list_1_max_degree=find_max_degree(ex_list_1)
ex_list_2_max_degree=find_max_degree(ex_list_2)
if ex_list_1_max_degree>=ex_list_2_max_degree:
    stroke=result(ex_list_1,ex_list_2)
elif ex_list_2_max_degree>ex_list_1_max_degree:
    stroke=result(ex_list_2,ex_list_1)
print(stroke)
with open("file_3.txt", "w") as f:
    f.write(stroke)
