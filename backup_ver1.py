# -*- coding: utf-8 -*-

import os
import time

source = ['C:\\1']
target_dir = 'C:\\Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Введите комментарий -->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
             comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Папка {0} создана'.format(today))



zip_command = 'WinRAR a {0} {1}'.format(target, ' '.join(source))
# zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

# C:\Backup\test C:\1

print(zip_command)

if os.system(zip_command) == 0:
    print('Успешный backup ' + target)

else:
    print('Мы всё потеряли')
