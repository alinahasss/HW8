import json
import os

def set_student(data_list):
    student_db[data_list[0]] = data_list[1:], {}

def see_rating(last_name, lessons, rating):
    if student_db.get(last_name) is None:
        print('Такого ученика нет в нашей базе')
        print(student_db)
    else:
        if lesson in student_db[last_name][1]:
            student_db[last_name][1][lesson].extend(rating)
        else:
            student_db[last_name][1][lesson] = rating


def get_student(last_name_student):
    if student_db.get(last_name_student) is None:
        print('Такого ученика нет в нашей базе')
    else:
        data = student_db[last_name_student]
        print(f'{last_name_student} {",".join(data[0])}:')
        print(*[f'{key}: {",".join(value)}' for key, value in data[1].items()], sep='\n')

def save_db():
    json.dump(student_db, open('db_student', 'w'))

def load_db():
    global student_db
    if os.stat('db_student.json').st_size == 0:
        student_db = {}
    else:
        student_db = json.load(open('db_student.json'))

lesson = input('Введите название предмета ')