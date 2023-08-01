# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

num = int(input('Enter the integer number: '))

n = num
base = 16
letters = '0123456789ABCDEF'
new = ''
 
while n > 0:
    n, remainder = divmod(n, base)
    new = letters[remainder] + new
 
print(new)

print('Check:' + hex(num))