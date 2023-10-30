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
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

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
        
        
