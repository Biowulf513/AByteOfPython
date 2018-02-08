# -*- coding: utf-8 -*-
from abc import *

class SchoolMember(metaclass=ABCMeta):
    '''Представление любого человека в школе'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    @abstractmethod
    def tell(self):
        '''Вывод информации'''
        print('Имя:"{name}" Возраст:"{age}"' \
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

# teach1 = Teacher('Марья Ивановна', 55, 35000)
# teach1.tell()

print('---Учитиля---')
s1 = Teacher('Иван Петренко', 18, 4)
s2 = Teacher('Иваdfgтренко', 48, 4)
s5 = Teacher('Иваxzcтренко', 58, 3)
s6 = Teacher('Ивxczxcренко', 68, 2)
s7 = Teacher('zxczxczxc', 78, 5)

print('---Ученики---')
t1 = Student('Иван Петренко', 18, 4)
t2 = Student('dr Петренко', 28, 3)
t3 = Student('Ивdfsdfан dfsтренко', 38, 5)
t4 = Student('Иван sdfо', 48, 4)
t5 = Student('Иsdfsdfs', 58, 3)
t6 = Student('Иsdfsdfренко', 68, 2)
t7 = Student('Ивdsfsdfетренко', 78, 5)

members = [s1, s2, s5, s6, s7, t1, t2, t3, t4, t5, t6, t7]
print('---Список---')
for member in members:
    member.tell()


