# -*- coding: utf-8 -*-
number = 23
running = True

while running:
    guess = int(input('Введите число '))

    if guess == number:
        print('Ты угадал')
        running = False
    elif guess < number:
        print('недобор')
    else:
        print('Перебор')
else:
    print('Цикл Закончен')

print('Я всё!')