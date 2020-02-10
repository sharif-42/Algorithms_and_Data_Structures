class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, value in enumerate(nums):
            remain = target - value
            if remain in nums and value != remain:
                return [index, lst.index(remain)]


lst = [2, 7, 11, 15]
target = 9
sln = Solution()
sln = sln.twoSum(lst, target)
print(sln)
matrix = [
    [0, 1, 2, 4],
    [0, 3, 1, 3],
    [0, 2, 3, 2],
    [0, 2, 4, 1],
    [0, 4, 1, 2],
    [0, 3, 2, 2],
    [1, 2, 2, 2]
]

n = len(matrix[0])
transpose = [[row[i] for row in matrix] for i in range(n)]
print(transpose)
