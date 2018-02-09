# -*- coding: utf-8 -*-

try:
    text = input('Введите текст: ')
except EOFError:
    print('Зачем ты всё отменил ?!')
except KeyboardInterrupt:
    print('Вы отменили операцию')
else:
    print('Вы ввели {0}'.format(text))
