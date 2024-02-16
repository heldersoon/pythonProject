class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def ever_grade(self):
        i = 0
        grade = 0
        for course in self.courses_in_progress:
            if course in self.grades:
                grade += sum(self.grades[course])
                i += len(self.grades[course])
            else:
                continue
        if i != 0:
            return round(grade / i, 1)
        else:
            return i


    def __str__(self):
        return (f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n'
        f'Средняя оценка домашнего задания: {self.ever_grade()}\n'
        f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
        f'Завершённые курсы: {",".join(self.finished_courses)}\n')

    def __lt__(self, other):
        if self.ever_grade() < other.ever_grade():
            return True
        else:
            return False

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    grades = {}
    def ever_grade(self):
        i = 0
        grade = 0
        for course in self.courses_attached:
            if course in self.grades:
                grade += sum(self.grades[course])
                i += len(self.grades[course])
            else:
                continue
        if i != 0:
            return round(grade / i, 1)
        else:
            return i

    def __str__(self):
        return (f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n'
        f'Средняя оценка за лекцию: {self.ever_grade()}\n')

    def __lt__(self, other):
        if self.ever_grade() < other.ever_grade():
            return True
        else:
            return False



class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in student.courses_in_progress
                and course in self.courses_attached):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n'f'Фамилия: {self.surname}\n'

# начало 4 -го задания

# создаём по 2 объекта каждого класса

student1 = Student("Maria","Petrova","woman")
student1.courses_in_progress = ["Python", "Git", "ООП", "Работа с файловой системой"]
student1.finished_courses = ["Введение в программирование"]

student2 = Student("Anton", "Sokolov", "man")
student2.courses_in_progress = ["Python", "Git", "ООП", "Работа с файловой системой"]
student2.finished_courses = ["Введение в программирование"]

lecturer1 = Lecturer("Oleg", "Ivanov")
lecturer1.courses_attached = ["Python", "Работа с файловой системой"]

lecturer2 = Lecturer("Sergey", "Smirnov")
lecturer2.courses_attached = ["Git", "ООП"]

reviewer1 = Reviewer('Pavel', 'Eman')
reviewer1.courses_attached = ["Работа с файловой системой", "Git"]

reviewer2 = Reviewer('Anatoly', 'Voronov')
reviewer2.courses_attached = ["ООП", "Python"]

# Оценки студентам за домашние задания

reviewer2.rate_hw(student1, "Python", 9)
reviewer2.rate_hw(student1, "Python", 8)
reviewer2.rate_hw(student1, "Python", 9)
reviewer2.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student1, "Git", 9)
reviewer1.rate_hw(student1, "Git", 8)
reviewer2.rate_hw(student1, "ООП", 8)
reviewer2.rate_hw(student1, "ООП", 9)
reviewer2.rate_hw(student1, "ООП", 7)
reviewer1.rate_hw(student1, "Работа с файловой системой", 9)

reviewer2.rate_hw(student2, "Python", 9)
reviewer2.rate_hw(student2, "Python", 8)
reviewer2.rate_hw(student2, "Python", 8)
reviewer2.rate_hw(student2, "Python", 9)
reviewer1.rate_hw(student2, "Git", 8)
reviewer1.rate_hw(student2, "Git", 7)
reviewer2.rate_hw(student2, "ООП", 8)
reviewer2.rate_hw(student2, "ООП", 8)
reviewer2.rate_hw(student2, "ООП", 9)

# Оценки за лекции

student1.rate_hw(lecturer1, "Python", 9)
student1.rate_hw(lecturer1, "Python", 10)
student1.rate_hw(lecturer1, "Python", 10)
student1.rate_hw(lecturer1, "Python", 10)
student1.rate_hw(lecturer2, "Git", 9)
student1.rate_hw(lecturer2, "ООП", 9)
student1.rate_hw(lecturer2, "ООП", 10)
student1.rate_hw(lecturer1, "Работа с файловой системой", 10)

student2.rate_hw(lecturer1, "Python", 9)
student2.rate_hw(lecturer1, "Python", 9)
student2.rate_hw(lecturer1, "Python", 10)
student2.rate_hw(lecturer1, "Python", 10)
student2.rate_hw(lecturer2, "Git", 9)
student2.rate_hw(lecturer2, "ООП", 9)
student2.rate_hw(lecturer2, "ООП", 10)
student2.rate_hw(lecturer1, "Работа с файловой системой", 9)

# Проверка переопределения __str__ и вычисления средних оценок

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

# Проверка переопределения оператора lt для классов Student и Lecturer

if student1 < student2:
    print(f'Cредние оценки у {student1.name} {student1.surname} ниже, чем у {student2.name} {student2.surname}\n')
else:
    print(f'Cредние оценки у {student1.name} {student1.surname} выше, чем у {student2.name} {student2.surname}\n')

if lecturer2 < lecturer1:
    print(f'Cредние оценки у {lecturer2.name} {lecturer2.surname} ниже, чем у {lecturer1.name} {lecturer1.surname}\n')
else:
    print(f'Cредние оценки у {lecturer2.name} {lecturer2.surname} выше, чем у {lecturer1.name} {lecturer1.surname}\n')

# Подсчёт средней оценки домашних работ по всем студентам по конкретному курсу занятий

students = [student1, student2]

def hw_average(course, students):
    grade = 0
    i = 0
    for student in students:
        if course in student.grades:
            grade += sum(student.grades[course])
            i += len(student.grades[course])
        else:
            continue
    if i != 0:
        print(f'Cредняя оценка по {course} для всех студентов {round(grade / i, 1)}')
    else:
        print(f'Средняя оценка по {course} для всех студентов отсутствует')
    return
# Проверка для курсов Python и ООП

hw_average("Python", students)
hw_average("ООП", students)

# Средняя оценка по курсу для лекторов

lecturers = [lecturer1, lecturer2]

def l_average(course, lecturers):
    grade = 0
    i = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            grade += sum(lecturer.grades[course])
            i += len(lecturer.grades[course])
        else:
            continue
    if i != 0:
        print(f'Cредняя оценка по {course} для всех лекторов {round(grade / i, 1)}')
    else:
        print(f'Средняя оценка по {course} для всех лекторов отсутствует')
    return

#
l_average("Python", lecturers)
l_average("ООП", lecturers)















