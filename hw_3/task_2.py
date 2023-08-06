# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

from array import array

my_list = [1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7]
print(my_list)

res = set()
for i in my_list:
    repetition = my_list.count(i)
    if repetition > 1:
        res.add(i)
print(res)