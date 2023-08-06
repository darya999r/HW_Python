# 1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

text = r'N:\GEEKBRAINS\Python\sem\106.py'

def file_path(text):
    *path, name = text.split('\\')
    name = list(name.split('.'))
    path = '\\'.join(path)
    return path, name[0], name[1]

print(file_path(text))