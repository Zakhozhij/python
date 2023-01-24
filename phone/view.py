def view_data(data):
    print(f'{data}')

def select_action():
    print('----------------\nВыберите действие:\n1.Добавить запись\n2.Вывести все записи\n3.Показать все записи отсортированные по id(По убыванию)\n4.Показать все записи отсортированные по id(По возрастанию)\n5.Показать все записи (только имена и фамилии)\n6.Выйти\n----------------')
    n=int(input("Введите n:"))
    return n

def init_value():
    id=int(input("Введите id:"))
    first_name=str(input("Введите имя:"))
    second_name=str(input("Введите фамилию:"))
    phone_number=str(input("Введите номер телефона:"))
    komment=str(input("Введите комментарий:"))
    return str(id)+"/"+first_name+"/"+second_name+"/"+phone_number+"/"+komment

def view_records(data):
    for val in data:
        print(" ".join(" ".join(val).split(';')))


def view_records_sorted_by_id(data,sort):
    if sort==1:
        rev=True
    else:
        rev=False
    for val in sorted(data, key=lambda v: " ".join(v).split(';')[0], reverse=rev):
        print(" ".join(" ".join(val).split(';')))
        

def view_records_names(data):
    for val in data:
        rec=" ".join(val).split(';')
        print(rec[1],rec[2])