import csv
def init_records(data):
    first_name=data.split('/')[0]
    second_name=data.split('/')[1]
    phone_number=data.split('/')[2]
    komment=data.split('/')[3]
    with open('phone/phone.csv','a+', encoding='UTF8') as file:
        file.write('{};{};{};{};{}\n'
                        .format(len(list(csv.reader(open("phone/phone.csv")))),first_name,second_name,phone_number,komment))
