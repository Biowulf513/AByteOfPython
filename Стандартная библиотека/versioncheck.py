# -*- coding: utf-8 -*-
import sys

correct_version = 3
runing_version = sys.version_info[0]

if runing_version < correct_version:
    print('Нужна {0} версия пайтона, а у тебя {1}'.format(correct_version, runing_version))
else:
    print('У тебя нужная %s версия Пайтона' %(runing_version))
