from collections import namedtuple
import argparse
import os
from Log import logger

# запуск из командной строки: # python N:\GEEKBRAINS\Python\hw\HW_Python\hw_15\Task_final.py -p N:\GEEKBRAINS\Python\hw\HW_Python

FilesObject = namedtuple('FilesObject', 'name ext is_dir parent', defaults=['', '', False, ''])

def parse_ars():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', metavar='path', type=str, nargs='*')
    args = parser.parse_args()
    return args.p

def path(path_str):
    files_objects = []
    path_str = os.path.abspath('hw_15')
    parent = path_str.rstrip('\\').rsplit('\\', 1)[1]
    try:
        for item in os.listdir(path_str):
            obj_name, obj_ext = None, None
            item: str = item.rsplit('\\', 1)[0]
            if item.rfind('.') != -1 and not item.startswith('.'):
                obj_name, obj_ext = item.rsplit('.', 1)
            else:
                obj_name = item
            files_objects.append(FilesObject(name=obj_name, ext=obj_ext, parent=parent, is_dir=False))
        logger.info(msg=str(files_objects[-1]))
    except Exception as exc:
        print(f'\033[31mERRORR: {exc.__class__.__name__}: {exc}\033[0m')
        logger.error(msg=f'{exc.__class__.__name__}: {exc}')
    return files_objects

if __name__ == '__main__':
    for folder in parse_ars():
        for item in (path(folder)):
            print(repr(item))

