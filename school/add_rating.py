import csv
def add_rating_to_student(data):
    with open('school/rating.csv','a+', encoding='UTF8') as file:
        for val in data:
            file.write('{}\n'
                        .format(val))

