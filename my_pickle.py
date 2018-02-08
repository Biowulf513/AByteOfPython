# -*- coding: utf-8
# import time
import pickle
# Имя файла в который мы сохраним объект
shoplistfile = 'shoplist.data'

# Список покупок
shop_list = ['яблоки','бананы','мясо','икра']

# запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shop_list, f)
f.close()

# Удаляем переменную
del shop_list
#
# # загружаем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print('из хранилища загрузили')
print(storedlist)