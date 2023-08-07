# 1. Доработаем задачи 5-6. Создайте класс-фабрику. 
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа. 
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_age(self, age):
        return self.age

    def get_name(self, name):
        return self.name


class Fish(Animal):
    def __init__(self, name, age, depth):
        super().__init__(name, age)
        self.depth = depth
        self.type = self.check_type()

    def check_type(self):
        return ("Мелководная", "Глубоководная")[self.depth > 1000]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nГлубина: {self.depth}\nТип: {self.type}\n'


class Bird(Animal):
    def __init__(self, name, age, wings):
        super().__init__(name, age)
        self.wings = wings
        self.type = self.check_type()

    def check_type(self):
        return ("Небольшой размах", "Большой размах")[self.wings > 3]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nРазмах крыльев: {self.wings}\nТип: {self.type}\n'


class Mammals(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight
        self.type = self.check_type()

    def check_type(self):
        return ("Мелкий", "Крупный")[self.weight > 100]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nВес: {self.weight}\nТип: {self.type}\n'


class AnimalFabric:

    def __init__(self, animal_class: str, **kwargs):
        self.animal_class = animal_class

        for key, value in kwargs.items():
            if key == 'name':
                self.name = value
            if key == 'age':
                self.age = value
            if key == 'depth':
                self.depth = value
            if key == 'wings':
                self.wings = value
            if key == 'weight':
                self.weight = value

    def get_info_animal(self):
        if self.animal_class == 'bird':
            return Bird(self.name, self.age, self.wings)
        elif self.animal_class == 'mammal':
            return Mammals(self.name, self.age, self.weight)
        elif self.animal_class == 'fish':
            return Fish(self.name, self.age, self.depth)
        else:
            return f'На фабрике нет такого животного'


animal_1 = AnimalFabric(animal_class='bird', name='Кеша', age=2, wings=2).get_info_animal()
print(animal_1)

animal_2 = AnimalFabric(animal_class='mammal', name='Мурзик', age=7, weight=3).get_info_animal()
print(animal_2)

animal_3 = AnimalFabric(animal_class='fish', name='Немо', age=1, depth=100).get_info_animal()
print(animal_3)