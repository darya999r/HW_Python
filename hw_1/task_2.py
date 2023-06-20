# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


lst = []
    
for i in range (3):
    side = int(input('Enter the side of the triangle: '))
    i = lst.append(side)
print(lst)


if lst[0] <= lst[1] + lst[2] and lst[1] <= lst[0] + lst[2] and lst[2] <= lst[0] + lst[1]:
    if lst[0] == lst[1] or lst[1] == lst[2] or lst[0] == lst[2]:
        res = 'It is an isosceles triangle!' # равнобедренный треугольник
    elif lst[0]*lst[0] == lst[1]*lst[1] == lst[2]*lst[2]:
        res = 'It is an equilateral triangle!' # равносторонний треугольник
    else:
        res = 'There is versatile triangle!' # разносторонний треугольник
else:
    res = 'There is no triangle!'

print(res)
