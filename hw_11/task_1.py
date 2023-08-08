# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
import time


class MyStr(str):
    '''Принимает строку и имя автора, возвращает строку, имя автора и время записи'''
    def __new__(cls, value, name):
        '''Создает экземпляр класса с атрибутом строки.
        Создает метку времени записи строки.
        Возвращает новый экземпляр.'''
        instance = super().__new__(cls, value)
        instance.value = value
        instance.name = name
        instance.start_time = time.time()
        return instance
    
    def __str__(self):
        '''Принимает объект класса, возвращает строковый вывод строки, имени автора и времени записи.'''
        return f'Str: {self.value}; autor: {self.name}; time: {self.start_time}'
    
    def __repr__(self):
        '''Принимает объект класса, возвращает печатное представление данного объекта.
        Т.е. вернет строку с атрибутами Str, autor, time.'''
        return f'(Str: {self.value}; autor: {self.name}; time: {self.start_time})'
    

str_1 = MyStr('First', 'Alex')
print(str_1)

str_2 = MyStr('Second', 'Oleg')
print(str_2)

