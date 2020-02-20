class Solution:
    def subsets(self, nums):
        power_set = []
        power_set.append([])
        print(power_set)
        n = len(nums)


if __name__ == '__main__':
    nums = [1, 2, 3]
    sln = Solution()
    print(sln.subsets(nums=nums))
