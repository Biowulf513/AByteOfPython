# -*- coding: utf-8 -*-

class ShortInputException(Exception):
    '''Пользовательский класс исключения'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Введите текст --> ')
    atleast = 8
    if len(text) < atleast:
        raise ShortInputException(len(text), atleast)
except EOFError:
    print('Ты прервал мою работу')
except KeyboardInterrupt:
    print('Ты прервал мою работу')
except ShortInputException as ex:
    print('Твой текст слишком мал, его длина {0}, а нужно минимум {1}'\
          .format(ex.length, ex.atleast))
else:
    print('Всё хорошо')