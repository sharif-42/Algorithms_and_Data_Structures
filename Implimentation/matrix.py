"""
All matrix Operations
"""
matrix = [
    [1, 2, 3, 1, 1],
    [4, 5, 6, 1, 1],
    [6, 7, 8, 1, 1],
    [9, 9, 9, 1, 1],
    [9, 9, 9, 1, 1],
    [9, 9, 9, 1, 1],
    [9, 9, 9, 1, 1],
    [9, 9, 9, 1, 1],
    [9, 9, 9, 1, 1],
]
##########################################################
#                   Transpose of Matrix                  #
##########################################################

# Using List Comprehension
transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose_matrix)

# Using Manual Coding
transpose_matrix_2 = []
for i in range(len(matrix[0])):
    lst = []
    for j in range(len(matrix)):
        lst.append(matrix[j][i])
    transpose_matrix_2.append(lst)
print(transpose_matrix_2)

########################################################
#                     Diagonal  Matrix                 #
########################################################
diagonal_matrix = []
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        if i == j:
            diagonal_matrix.append(matrix[i][i])

print(diagonal_matrix)
diagonal_matrix = [matrix[i][j] for j in range(len(matrix)) for i in range(len(matrix[0])) if i == j]
print(diagonal_matrix)
