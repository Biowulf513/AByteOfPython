# -*- coding: utf-8 -*-
import sys

print('Аргументы командной строки: ')
for i in sys.argv:
    print(i)

print('\nПеременная PYTHONPATH содержат', sys.path, '\n')
