# -*- coding: utf-8 -*-
import os, platform, logging, time

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
                                os.getenv('HOMEPATH'), \
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print('Сохраняем лог в', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
)

logging.debug('Начало программы')
time.sleep(1)
logging.info('Какие-то действия')
time.sleep(3)
logging.warning('Программа умирает')
