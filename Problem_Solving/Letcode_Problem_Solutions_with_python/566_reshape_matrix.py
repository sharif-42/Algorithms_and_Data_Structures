class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        flat_matrix = []
        matrix = []
        x = len(mat)
        y = len(mat[0])
        if r * c != x * y:
            return mat

        for i in range(x):
            for j in range(y):
                flat_matrix.append(mat[i][j])

        for i in range(r):
            row = []
            for j in range(c):
                row.append(flat_matrix[(c * i) + j])
            matrix.append(row)

        return matrix


if __name__ == "__main__":
    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    s = Solution().matrixReshape(mat, r, c)
    print(s)
