class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_grade(self):
        ls_gr = list(self.grades.values())
        if len(ls_gr) == 1:
            av_gr = sum(ls_gr[0]) / len(ls_gr[0])
            return round(av_gr, 1)
        else:
            av_gr_ls = []
            for i in range(len(ls_gr)):
                a = sum(ls_gr[i]) / len(ls_gr[i])
                av_gr_ls.append(a)
            av_gr = sum(av_gr_ls) / len(av_gr_ls)
            return round(av_gr, 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
               f'{self.__average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        return self.__average_grade() < other.__average_grade()

    def __le__(self, other):
        return self.__average_grade() <= other.__average_grade()

    def __gt__(self, other):
        return self.__average_grade() > other.__average_grade()

    def __ge__(self, other):
        return self.__average_grade() >= other.__average_grade()

    def __eq__(self, other):
        return self.__average_grade() == other.__average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_grade(self):
        ls_gr = list(self.grades.values())
        if len(ls_gr) == 1:
            av_gr = sum(ls_gr[0]) / len(ls_gr[0])
            return round(av_gr, 1)
        else:
            av_gr_ls = []
            for i in range(len(ls_gr)):
                a = sum(ls_gr[i]) / len(ls_gr[i])
                av_gr_ls.append(a)
            av_gr = sum(av_gr_ls) / len(av_gr_ls)
            return round(av_gr, 1)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}'

    def __lt__(self, other):
        return self.__average_grade() < other.__average_grade()

    def __le__(self, other):
        return self.__average_grade() <= other.__average_grade()

    def __gt__(self, other):
        return self.__average_grade() > other.__average_grade()

    def __ge__(self, other):
        return self.__average_grade() >= other.__average_grade()

    def __eq__(self, other):
        return self.__average_grade() == other.__average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_grade_course_st(student, course):
    av_gr = sum(student.grades[course]) / len(student.grades[course])
    print(f'Средняя оценка по курсу {course} студента {student.name} {student.surname} составляет {round(av_gr, 1)}')
    return round(av_gr, 1)

def average_grade_course_lect(lecturer, course):
    av_gr = sum(lecturer.grades[course]) / len(lecturer.grades[course])
    print(f'Средняя оценка по курсу {course} лектора {lecturer.name} {lecturer.surname} составляет {round(av_gr, 1)}')
    return round(av_gr, 1)





best_student = Student('Дмитрий', 'Краснов', 'мужчина')
best_student.courses_in_progress += ['Python']

best_student.courses_in_progress += ['JavaScript']

best_student.finished_courses += ['Введение в программирование']
student_2 = Student('Елена', 'Пушилина', 'женщина')
student_2.courses_in_progress += ['JavaScript']
student_2.finished_courses += ['Введение в программирование']

cool_reviewer_1 = Reviewer('Иван', 'Иванов')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_2 = Reviewer('Алексей', 'Кузнецов')
cool_reviewer_2.courses_attached += ['JavaScript']

cool_mentor_1 = Mentor('Some', 'Buddy')
cool_mentor_1.courses_attached += ['Python']
cool_mentor_2 = Mentor('Another', 'Buddy')
cool_mentor_2.courses_attached += ['JavaScript']

cool_lecturer_1 = Lecturer('Борис', 'Палюх')
cool_lecturer_1.courses_attached += ['Python']
cool_lecturer_2 = Lecturer('Дмитрий', 'Мартынов')
cool_lecturer_2.courses_attached += ['JavaScript']

cool_reviewer_1.rate_hw(best_student, 'Python', 10)
cool_reviewer_1.rate_hw(best_student, 'Python', 10)
cool_reviewer_1.rate_hw(best_student, 'Python', 10)
cool_reviewer_2.rate_hw(student_2, 'JavaScript', 9)
cool_reviewer_2.rate_hw(student_2, 'JavaScript', 7)
cool_reviewer_2.rate_hw(student_2, 'JavaScript', 10)


cool_reviewer_2.rate_hw(best_student, 'JavaScript', 10)
cool_reviewer_2.rate_hw(best_student, 'JavaScript', 10)
cool_reviewer_2.rate_hw(best_student, 'JavaScript', 10)


best_student.rate_hw(cool_lecturer_1, 'Python', 10)
best_student.rate_hw(cool_lecturer_1, 'Python', 10)
best_student.rate_hw(cool_lecturer_1, 'Python', 10)
student_2.rate_hw(cool_lecturer_2, 'JavaScript', 8)
student_2.rate_hw(cool_lecturer_2, 'JavaScript', 7)
student_2.rate_hw(cool_lecturer_2, 'JavaScript', 10)


print(best_student > student_2)
print(cool_lecturer_1 < cool_lecturer_2)
print(best_student)
print(student_2)
print(cool_lecturer_1)
print(cool_lecturer_2)
print(cool_reviewer_1)
print(cool_reviewer_2)

average_grade_course_st(best_student, 'Python')
average_grade_course_lect(cool_lecturer_1, 'Python')
average_grade_course_st(student_2, 'JavaScript')
average_grade_course_lect(cool_lecturer_2, 'JavaScript')
