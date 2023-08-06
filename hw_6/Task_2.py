# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.

import random
from Module_Chess.Module_Chess_2 import conflict,queens,queenprint

print('Всего успешных расстоновок: ' + str(len(list(queens()))))
print()
print('Один вариант успешной расстановки:')
queenprint(random.choice(list(queens())))