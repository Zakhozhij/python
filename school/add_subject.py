import csv
def add_subject(data):
    with open('school/subjects.csv','a+', encoding='UTF8') as file:
        for val in data:
            file.write('{};{}\n'
                        .format(len(open("school/subjects.csv").readlines())+1,val))

