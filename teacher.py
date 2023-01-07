from student_database import set_student, see_rating

def add_st():
    m = input('Введите данные (Фамилия, Имя, класс):').split('')
    set_student(m)

def add_score():
    last_name = input('Введите фамилию ученика: ')
    lesson = input('Введите название предмета: ')
    rating = input('Введите оценку ').split()
    see_rating(last_name, lesson, rating)