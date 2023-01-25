from random import randint
def select_action():
    print('----------------\
        \nВыберите действие:\
        \n1.Добавить студента вручную\
        \n2.Добавить 100 случайных студентов и рандомные им оценки\
        \n3.Добавить предмет\
        \n4.Добавить оценку ученику по предмету\
        \n5.Показать список учеников\
        \n6.Показать лист оценок ученика\
        \n7.Вывести среднюю оценку ученика по предмету\
        \n8.Вывести среднюю оценку по школе по конкретному предмету\
        \n9.Вывести количество учеников претендующих на золотую медаль\
        \n10.Выйти\n----------------')
    n=int(input("Введите n:"))
    return n

def view_data(data):
    print(f'{data}')

def add_student():
    add_student=[]
    first_name=str(input("Введите имя:"))
    second_name=str(input("Введите фамилию:"))
    add_student.append(first_name+" "+second_name)
    return add_student

def add_student_one_hundred_random_students():
    add_student=[]
    first_names=['Егор','Максим','Андрей','Саша','Толя','Владимир','Артур','Олег','Дима','Влад']
    second_names=['Семенов','Егоров','Дюжев','Снитко','Васнецов','Горев','Смирнов','Чехов','Иванов','Петров']
    for _ in range(1,10):
        add_student.append(first_names[randint(0, 9)]+" "+second_names[randint(0, 9)])
    return add_student


def add_subject():
    add_subject=[]
    add_subject.append(str(input("Введите название предмета:")))
    return add_subject

def view_students(data):
    for val in data:
        print(" ".join(" ".join(val).split(';')))

def view_subjects(data):
    for val in data:
        print(" ".join(" ".join(val).split(';')))

def select_student(last_student_id):
    x=False
    while x!=True:
        print('Выберите id студента')
        id=int(input("Введите id:"))
        if id<1 or id>last_student_id:
            x=False
        else:
            x=True
    return id

def select_subject(last_subject_id):
    x=False
    while x!=True:
        print('Выберите id предмета')
        id=int(input("Введите id:"))
        if id<1 or id>last_subject_id:
            x=False
        else:
            x=True
    return id

def add_rating():
    x=False
    while x!=True:
        r=int(input("Введите оценку 1-5:"))
        if r<1 or r>5:
            x=False
        else:
            x=True
    return r

def add_random_rating(last_student_id_before,last_student_id_after,last_subject_id):
    random_ratings=[]
    for i in range(last_student_id_before+1,last_student_id_after+1):
        random_ratings.append(str(i)+";"+str(randint(1,last_subject_id))+";"+str(randint(1, 5)))
    return random_ratings

def show_student_info(student_info,rating_info,subjects):
    print('Оценки ученика:'+student_info)
    subjects_names={}
    for i in subjects:
        subjects_names["".join(i).split(';')[0]] = "".join(i).split(';')[1]
    for i in rating_info:
        print(subjects_names["".join(i).split(';')[0]],"->","".join(i).split(';')[1])

def show_middle_rating_of_student_info(student_info,middle_rating_info,subject_info):
    print('Средняя оценка ученика:'+str(student_info)+' по предмету:'+str(subject_info)+'->'+str(middle_rating_info))

def show_middle_rating_of_school_info(middle_rating_info,subject_info):
    print('Средняя оценка школы по предмету:'+str(subject_info)+'->'+str(middle_rating_info))

def show_count_best_students(count_best):
    print('Количество учеников претендующих на золотую медаль->'+str(count_best))