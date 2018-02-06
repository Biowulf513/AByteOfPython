# -*- coding: utf-8 -*-
class Robot:
    '''Представляет робота с именем.'''
    # Переменная класса
    population = 0

    def __init__(self, name):
        '''Иницилизация данных'''
        self.name = name
        print('(Иницилизация {0})'.format(self.name))

        # При создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.population += 1

    def __del__(self):
        '''Убиваем робота'''
        print('{0} уничтожается'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print ('Славный {0} был последним представителем рода'\
                   .format(self.name))
        else:
            print ('Друже {0} унечтожен, осталось {1} роботов'\
                   .format(self.name, Robot.population))

    def sayHi(self):
        '''Приветствие робота'''
        print('Приветствую тебя хозяин, ты назвал меня {0}'.format(self.name))

    def howMany():
        '''Вывод кол-ва роботов'''
        print('Всего в наличии {0} роботов'.format(Robot.population))

    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

droid3 = Robot('Электроник')
droid3.sayHi()
Robot.howMany()

print('==================')
#
# del droid1
# del droid2