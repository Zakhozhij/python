import add_students as add_stud
import add_subject as add_sub
import output_data as out_data
import add_rating as add_rat
import view

def select_action():
    
    n=view.select_action()
    if n==1:
        add_student()
    elif n==2:
        add_student_one_hundred_random_students()
    elif n==3:
        add_subject()
    elif n==4:
        add_rating()
    elif n==5:
        get_all_students()
    elif n==6:
        get_all_ratings_of_student()
    elif n==7:
        get_middle_rating_of_student()
    elif n==8:
        get_middle_rating_of_school()
    elif n==9:
        get_count_best_students()
    if n!=10:
        select_action()

def add_student():
    data=view.add_student()
    add_stud.add_student(data)
    view.view_data(data)

def add_student_one_hundred_random_students():
    data=view.add_student_one_hundred_random_students()
    last_student_id_before=out_data.get_last_student_id()
    add_stud.add_student(data)
    last_student_id_after=out_data.get_last_student_id()
    last_subject_id=out_data.get_last_subject_id()
    data=view.add_random_rating(last_student_id_before,last_student_id_after,last_subject_id)
    add_rat.add_rating_to_student(data)

def add_subject():
    data=view.add_subject()
    add_sub.add_subject(data)
    view.view_data(data)

def add_rating():
    data=out_data.get_students()
    view.view_students(data)
    last_student_id=out_data.get_last_student_id()
    student_id=view.select_student(last_student_id)
    data=out_data.get_subjects()
    view.view_subjects(data)
    last_subject_id=out_data.get_last_subject_id()
    subject_id=view.select_subject(last_subject_id)
    rating=view.add_rating()
    add_rat.add_rating_to_student([str(student_id)+";"+str(subject_id)+";"+str(rating)])
    select_action()

def get_all_students():
    data=out_data.get_students()
    view.view_students(data)

def  get_all_ratings_of_student():
    data=out_data.get_students()
    view.view_students(data)
    last_student_id=out_data.get_last_student_id()
    student_id=view.select_student(last_student_id)
    student_info=out_data.get_student_info(student_id)
    rating_info=out_data.get_rating_info(student_id)
    subjects=out_data.get_subjects()
    view.show_student_info(student_info,rating_info,subjects)

def get_middle_rating_of_student():
    data=out_data.get_students()
    view.view_students(data)
    last_student_id=out_data.get_last_student_id()
    student_id=view.select_student(last_student_id)
    student_info=out_data.get_student_info(student_id)
    data=out_data.get_subjects()
    view.view_subjects(data)
    last_subject_id=out_data.get_last_subject_id()
    subject_id=view.select_subject(last_subject_id)
    subject_info=out_data.get_subject_info(subject_id)
    middle_rating_info=out_data.get_middle_rating_info_for_subject(student_id,subject_id)
    view.show_middle_rating_of_student_info(student_info,middle_rating_info,subject_info)

def get_middle_rating_of_school():
    data=out_data.get_subjects()
    view.view_subjects(data)
    last_subject_id=out_data.get_last_subject_id()
    subject_id=view.select_subject(last_subject_id)
    subject_info=out_data.get_subject_info(subject_id)
    middle_rating_info=out_data.get_middle_rating_of_school(subject_id)
    view.show_middle_rating_of_school_info(middle_rating_info,subject_info)

def get_count_best_students():
    count_best=out_data.get_count_best_students()
    view.show_count_best_students(count_best)