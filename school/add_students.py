def add_student(data):
    with open('school/students.csv','a+', encoding='UTF8') as file:
        count_rows=len(open("school/students.csv", encoding='UTF8').readlines())
        for val in data:
            count_rows+=1
            file.write('{};{}\n'
                        .format(count_rows,val))

