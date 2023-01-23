import csv
def get_records():
    with open('phone/phone.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        list_records.pop(0)
        return list_records