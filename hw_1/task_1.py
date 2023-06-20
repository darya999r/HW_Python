# Выведите в консоль таблицу умножения 
# от 2х2 до 9х10 как на школьной тетрадке.

text = 'ТАБЛИЦА УМНОЖЕНИЯ'
print(text.center(50))
 
for i in range(1, 11):
    for k in range(2, 6):
        if i * k // 10 < 1:
            print(f'{k} * {i}=  {i * k}\t', end='')
        elif i == 10:
            print(f'{k} * {i}={i * k}\t', end='')
        else:
            print(f'{k} * {i}= {i * k}\t', end='')
    print('')
print('  ')
for i in range(1, 11):
    for k in range(6, 10):
        if i * k // 10 < 1:
            print(f'{k} * {i}=  {i * k}\t', end='')
        elif i == 10:
            print(f'{k} * {i}={i * k}\t', end='')
        else:
            print(f'{k} * {i}= {i * k}\t', end='')
    print('')
    