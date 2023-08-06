# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.

things = {'tent': 10,
          'sleeping_bag': 2,
          'barbecue': 5,
          'matches': 0.1,
          'axe': 1,
          'lantern': 0.3,
          'knife': 0.2,
          'compass': 0.1,
          }

print(f'Наш список вещей: {things}')
backpack = float(input('Enter maximum load capacity of the backpack in kg (integer or float number): '))
sum = backpack
new_backpack = {}

for key, value in things.items():
    if value <= sum:
        sum -= value
        new_backpack[key] = value

print(f"Backpack capacity {backpack} kg. Possible complete set of the backpack: {new_backpack}")