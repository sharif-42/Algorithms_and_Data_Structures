n = 3
m = 4
a = [[0] * m] * n
a[0][0] = 0
print(a)

# Initialize matrix
matrix = []
R = 2
C = 3
# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()
