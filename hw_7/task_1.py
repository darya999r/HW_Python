#  1 — Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. 
#   При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла. 
#   Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

import os
from pathlib import Path


def group_rename(count_len: int, extension: str, new_extension: str, interval: list[int], new_name=''):
    count = 0
    for file in os.listdir():
        if file.endswith(extension):
            count += 1
            Path(file).rename(f"{file.split('.')[0][interval[0]:interval[1]]}{new_name}{count:0>{count_len}}.\
{new_extension}")  #переименование файла по условию


group_rename(3, 'zip', 'avi', [0, 2], "ZORRO")