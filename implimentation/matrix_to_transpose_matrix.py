if __name__=='__main__':
    matrix = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    ]

    # Using Row Coding
    transpose = []
    for i in range(4):
        lst = []
        for j in matrix:
            lst.append(j[i])
        transpose.append(lst)
    print(transpose)

    # Using List Comprehension
    transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(transpose_matrix)

    """
    We Can Also Do this by using Pandas and Scikit Learn Libraries
    """