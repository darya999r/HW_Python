# 2. Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9], 
        ]

print('Parent matrix: ')
for element in matrix:
    print(*element, sep='\t')

print()

print('Transposed matrix: ')
for element in zip(*matrix):
    print(*element, sep='\t')