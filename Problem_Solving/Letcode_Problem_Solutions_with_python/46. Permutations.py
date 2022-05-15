class Solution:
    def permute(self, nums):
        # n = len(nums)
        # res = []
        # if n == 1:
        #     return [nums]
        # for i in range(n):
        #     for j in range(n - 1):
        #         nums[0], nums[j + 1] = nums[j + 1], nums[0]
        #         res = res + [nums[:]]
        # return res

        n = len(nums)
        if n == 0:
            return []

        if n == 1:
            return [nums]

        l = []

        for i in range(len(nums)):
            m = nums[i]
            print(m, nums[:i],  nums[i + 1:])
            remLst = nums[:i] + nums[i + 1:]

            for p in self.permute(remLst):
                l.append([m] + p)
        print(l)
        return l



if __name__ == '__main__':
    nums = [5,4,6,2]
    sln = Solution()
    print(sln.permute(nums=nums))
