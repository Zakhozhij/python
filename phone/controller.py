import export_data as exd
import import_data as imd
import view

def select_action():
    n=view.select_action()
    if n==1:
        add_record()
    elif n==2:
        get_records()
    elif n==3:
        get_sorted_records_by_id()
    elif n==4:
        get_records_names()
    else:
        print('Действия не существует!')

def add_record():
    data=view.init_value()
    imd.init_records(data)
    view.view_data(data)

def get_records():
    data=exd.get_records()
    view.view_records(data)

def get_sorted_records_by_id():
    data=exd.get_records()
    view.view_records_sorted_by_id(data)

def get_records_names():
    data=exd.get_records()
    view.view_records_names(data)