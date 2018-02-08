# -*- coding: utf-8 -*-

class SchoolMember:
    '''Представление любого человека в школе'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))
    def tell(self):
        '''Вывести информацию'''
        print('Имя:"{name}" Возраст:"{age}"'\
            .format(name=self.name, age=self.age), end=' ')
class Teacher(SchoolMember):
    '''Представление преподователя.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан учитель {name})'.format(name=self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0}"'.format(self.salary))

class Student(SchoolMember):
    '''Педставление студента'''
    def __init__(self, name, age, marsk):
        SchoolMember.__init__(self, name, age)
        self.marks = marsk
        print('(Создан ученик {name})'.format(name=self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки:"{marsk}"'.format(marsk=self.marks))

teach1 = Teacher('Марья Ивановна', 55, 35000)
teach1.tell()

student1 = Student('Иван Петренко', 18, 4)
# SchoolMember.tell(student1)
student1.tell()

