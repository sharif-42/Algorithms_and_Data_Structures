class Solution:
    def diagonalSum(self, mat) -> int:
        total = 0
        subtract = 0
        l = len(mat)
        if l % 2:
            subtract = mat[l // 2][l // 2]
        for i in range(1, l + 1):
            total = total + mat[i - 1][i - 1] + mat[i - 1][-i]
            print(mat[i - 1][i - 1], mat[i - 1][-i])

        return total - subtract


if __name__ == "__main__":
    arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    arr = [[1, 2, 3, 1, 1],
           [4, 5, 6, 1, 1],
           [7, 8, 10, 1, 1],
           [7, 8, 9, 1, 1],
           [7, 8, 9, 1, 1]]
    # arr = [[1, 1, 1, 1],
    #        [1, 1, 1, 1],
    #        [1, 1, 1, 1],
    #        [1, 1, 1, 1]]
    s = Solution().diagonalSum(arr)
    print(s)
