# -*- coding: utf-8 -*-
#Импорт
import zipfile
import os
import time
#Файлы для бекапа
backup_files = ['C:\\py\\1', 'C:\\py\\2']
#Место для бекапа
backup_folder = 'C:\\py\\Backup\\'+time.strftime('%d_%m_%Y')
#Название бекапа
zip_name = time.strftime('%H_%M_%S')+'.zip'
#Функция создания бекапа
zip_command = 'zipf'

if os.path.exists(backup_folder):
    print('Папка существует')
else:
    os.mkdir(backup_folder)
    print('Папки нет\nСоздаю папку', backup_folder)

def check_zip_create():
    pass


#функция проверки бекапа