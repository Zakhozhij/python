import csv
def get_students():
    with open('school/students.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        return list_records

def get_subjects():
    with open('school/subjects.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        return list_records

def get_last_student_id():
    count_rows=len(open("school/students.csv", encoding='UTF8').readlines())
    return count_rows

def get_last_subject_id():
    count_rows=len(open("school/subjects.csv", encoding='UTF8').readlines())
    return count_rows

def get_student_info(student_id):
    student_name=''
    with open('school/students.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        for i in list_records:
            if int("".join(i).split(';')[0])==student_id:
                student_name=" ".join(i).split(';')[1]
    return student_name

def get_rating_info(student_id):
    rating=[]
    with open('school/rating.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        for i in list_records:
            if int("".join(i).split(';')[0])==student_id:
                rating.append(str("".join(i).split(';')[1])+";"+str(int("".join(i).split(';')[2])))
    return rating

def get_middle_rating_info_for_subject(student_id,subject_id):
    rating=0
    k=0
    with open('school/rating.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        for i in list_records:
            if int("".join(i).split(';')[0])==student_id and int("".join(i).split(';')[1])==subject_id:
                rating+=int("".join(i).split(';')[2])
                k+=1
    if k==0:
        k=1
    return round(rating/k)

def get_subject_info(subject_id):
    subject_name=''
    with open('school/subjects.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        for i in list_records:
            if int("".join(i).split(';')[0])==subject_id:
                subject_name=" ".join(i).split(';')[1]
    return subject_name

def get_middle_rating_of_school(subject_id):
    rating=0
    k=0
    with open('school/rating.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        for i in list_records:
            if int("".join(i).split(';')[1])==subject_id:
                rating+=int("".join(i).split(';')[2])
                k+=1
    if k==0:
        k=1
    return round(rating/k)

def get_count_best_students():
    count_best=0
    with open('school/students.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        for i in list_records:
            is_best=True
            count_r=0
            with open('school/rating.csv','r', encoding='UTF8') as file_rat:
                list_ratings = list(csv.reader(file_rat))
                for lr in list_ratings:
                    if int("".join(lr).split(';')[0])==int("".join(i).split(';')[0]):
                        if int("".join(lr).split(';')[2])>=1 and int("".join(lr).split(';')[2])<=3:
                            is_best=False
                        count_r+=1
            if is_best==True and count_r>0:
                count_best+=1
    return count_best