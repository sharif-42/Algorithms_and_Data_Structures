class Solution:
    def findNumbers(self, nums):
        cnt = 0
        n = len(nums)
        for i in nums:
            cnt += (len(str(i)) % 2)

        return n - cnt


if __name__ == '__main__':
    nums = []
    sln = Solution().findNumbers(nums)
    print(sln)
