# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from math import gcd
import fractions
 
a, b = map(int, input('Enter first fraction of the form a/b : ').split('/'))
c, d = map(int, input('Enter second fraction of the form a/b : ').split('/'))
 
if b == d:
    print('{}/{}'.format(a+c, b))
else:
    cd = int(b*d/gcd(b, d))
    rn = int(cd/b*a+cd/d*c)
    g2 = gcd(rn, cd)
    n = int(rn/g2)
    d = int(cd/g2)
    print('{}/{}'.format(n, d) if n != d else n)


num1 = fractions.Fraction(a, b)
num2 = fractions.Fraction(c, d)
print(num1 + num2)