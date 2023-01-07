from student import see_rating
from student_database import load_db, save_db
from teacher import add_score, add_st


def controll():
    load_db()
    match input('1 - Учитель, 2 - Ученик: '):

        case '1':
            t = 1
            while t == 1:
                print('Ваши действия')
                act = input('1 - ввести ученика, 2 - проставить оценки, 3 - выйти\nВвод: ')
                if act == '1':
                    add_st()
                elif act == '2':
                    add_score()
                elif act == '3':
                    t = 0
            else:
                save_db()
        case '2':
            t = 1
            while t == 1:
                last_name = input('Введите свою фамилию или 3 для выхода из приложения\nВвод: ')
                if last_name == '3':
                    t = 0
                else:
                    see_rating(last_name)
