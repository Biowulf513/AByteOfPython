# -*- coding: utf-8 -*-
number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('Угадал')

elif guess < number:
    print('Недобор')

else:
    print('Перебор')

print('Конец !')
