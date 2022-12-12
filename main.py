#ДЗ на понедельник:
# Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых файла:
# test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os

import os

os.mkdir('C:/Users/Администратор/Desktop/Новая папка')
t1 = open('C:/Users/Администратор/Desktop/Новая папка/test_1.txt', 'w')
t2 = open('C:/Users/Администратор/Desktop/Новая папка/test_2.txt', 'w')
t3 = open('C:/Users/Администратор/Desktop/Новая папка/test_3.txt', 'w')

t1.close()
t2.close()
t3.close()

os.rename('C:/Users/Администратор/Desktop/Новая папка/test_1.txt', 'C:/Users/Администратор/Desktop/Новая папка/rename_1.txt')
os.rename('C:/Users/Администратор/Desktop/Новая папка/test_2.txt', 'C:/Users/Администратор/Desktop/Новая папка/rename_2.txt')
os.rename('C:/Users/Администратор/Desktop/Новая папка/test_3.txt', 'C:/Users/Администратор/Desktop/Новая папка/rename_3.txt')

os.remove('C:/Users/Администратор/Desktop/Новая папка/rename_1.txt')
os.remove('C:/Users/Администратор/Desktop/Новая папка/rename_2.txt')
os.remove('C:/Users/Администратор/Desktop/Новая папка/rename_3.txt')

os.rmdir('C:/Users/Администратор/Desktop/Новая папка')