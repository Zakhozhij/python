import csv
def init_records(data):
    id=data.split('/')[0]
    first_name=data.split('/')[1]
    second_name=data.split('/')[2]
    phone_number=data.split('/')[3]
    komment=data.split('/')[4]
    with open('phone/phone.csv','a+', encoding='UTF8') as file:
        file.write('{};{};{};{};{}\n'
                        .format(id,first_name,second_name,phone_number,komment))

def init_sorted_records_by_id(data,sort):
    if sort==1:
        rev=True
    else:
        rev=False
    with open('phone/phone.csv','w', encoding='UTF8') as file:
        file.write('id;name;second_name;phone_number;komment\n')
        for val in sorted(data, key=lambda v: " ".join(v).split(';')[0], reverse=rev):
            file.write('{}\n'
                        .format("".join(val)))