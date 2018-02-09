# -*- coding: utf-8 -*-
import time

try:
    file = open('../poem.txt')
    while True:
        line = file.readline()
        if len(line) == 0:
            print('\n=========END=========')
            break
        print(line, end='')
        time.sleep(1)

except KeyboardInterrupt:
    print('!!! Вы отменили чтение файла !!!')

finally:
    file.close()
    print('Закрытие файла')