class Solution:
    def checkXMatrix(self, grid) -> bool:
        n = len(grid)
        total = 0
        total_sum = 0
        for i in range(n):
            # print("test", i, n - i - 1)
            if grid[i][i] and grid[i][n - i - 1]:
                if i == (n - i - 1):
                    total = total + grid[i][i]
                else:
                    total = total + grid[i][i] + grid[i][n - i - 1]
            else:
                return False
            total_sum += sum(grid[i])
            # print(grid[i][i], grid[i][n - i - 1])
        # print(total, total_sum)
        if total_sum == total:
            return True
        else:
            return False


if __name__ == "__main__":
    grid = [[2, 0, 0, 1],
            [0, 3, 1, 0],
            [0, 5, 2, 0],
            [4, 0, 0, 2]]
    grid = [[5, 7, 0],
            [0, 3, 1],
            [0, 5, 0]]
    grid = [
        [1, 0, 0, 0, 2],
        [0, 3, 0, 4, 0],
        [0, 0, 5, 0, 0],
        [0, 6, 0, 7, 0],
        [8, 0, 0, 0, 9]
    ]
    grid = [[0, 0, 0, 0, 1],
            [0, 4, 0, 1, 0],
            [0, 0, 5, 0, 0],
            [0, 5, 0, 2, 0],
            [4, 0, 0, 0, 2]]
    solution = Solution().checkXMatrix(grid)
    print(solution)
