# Создайте класс Матрица. Добавьте методы для: вывода на печать, 
# проверку на равенство, сложения, *умножения матриц

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def get_matrix(self):
        return self.matrix
    
    def __str__(self):
        res = ''
        for i in range(len(self.matrix)):
            res += str(self.matrix[i]) + '\n'
        return res
    
    def compar_matrix(self, second_matrix):
        if len(self.matrix) != len(second_matrix.matrix) or len(self.matrix[0]) != len(second_matrix.matrix[0]):
            return f'Error! Нельзя сравнить матрицы разных размеров!'
        else:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if self.matrix[i][j] != second_matrix.matrix[i][j]:
                        return False
            return True
    
    def sum_matrix(self, second_matrix):
        if len(self.matrix) != len(second_matrix.matrix) or len(self.matrix[0]) != len(second_matrix.matrix[0]):
            return f'Error! Нельзя сложить матрицы разных размеров!'
        else:
            return Matrix([[self.matrix[i][j] + second_matrix.matrix[i][j] for j in range(len(self.matrix[0]))] \
                           for i in range(len(self.matrix))])
        
        
    def multipl_matrix(self, second_matrix):
        if len(self.matrix) != len(second_matrix.matrix) or len(self.matrix[0]) != len(second_matrix.matrix[0]):
            return f'Error! Нельзя умножить матрицы разных размеров!'
        else:
            res_matrix = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*second_matrix.matrix)] \
                        for i_row in self.matrix]
            return Matrix(res_matrix)
        
matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]]

matrix_2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]]

matrix_1 = Matrix(matrix_1)
matrix_2 = Matrix(matrix_2)

print('Матрицы равны? ')
print(matrix_1.compar_matrix(matrix_2))

print('Cложение матриц: ')
print(matrix_1.sum_matrix(matrix_2))

print('Умножение матриц: ')
print(matrix_1.multipl_matrix(matrix_2))
