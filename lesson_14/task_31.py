class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_info_about_group(self):
        for student in self.students:
            student.get_info()


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = []

    def change_name(self, name):
        self.name = name

    def change_surname(self, surname):
        self.surname = surname

    def add(self, *a):
        self.grades.extend(a)

    def get_info(self):
        print('Студент {} {} имеет оценки: {}'.format(self.name, self.surname, self.grades))


group1 = Group('First')
student_1 = Student('Николай', 'Бойко')
student_1.add(5, 10, 8, 9)
group1.add_student(student_1)
student_2 = Student('Петр', 'Иванов')
student_2.add(7, 8, 10, 12)
group1.add_student(student_2)
group1.display_info_about_group()
