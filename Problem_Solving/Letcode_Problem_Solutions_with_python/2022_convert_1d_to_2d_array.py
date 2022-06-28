class Solution:
    def construct2DArray(self, original, m: int, n: int):
        matrix = []
        if len(original) != m * n:
            return matrix
        for i in range(m):
            row_mat = []
            for j in range(n):
                row_mat.append(original[n * i + j])
            matrix.append(row_mat)
        return matrix


if __name__ == "__main__":
    mat = [1, 1, 1, 1]
    m = 4
    n = 1
    s = Solution().construct2DArray(mat, m, n)
    print(s)
