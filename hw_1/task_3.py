# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


num = input('Enter number: ')
if num.isdecimal() and 0 < (n:=int(num)) < 100000:
    
    if is_prime(n):
        print ('The number is not prime!')
    else:
        print ('The number is prime!')

else:
    print('Error. Enter a positiv integer up to 100000!')

