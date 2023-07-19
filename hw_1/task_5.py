# 5. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
counter = 0


while counter < 10:
    N = int(input('Enter a number between 0 and 1000: '))
    if N < num:
        print("More")
        counter = counter+1
    elif N > num:
        print("Less")
        counter = counter+1
    elif N == num:
        print("You've won!")
    else:
        print("Error")
else:
    print("You lose!")