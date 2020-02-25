class Solution:
    def subsets(self, nums):
        n = len(nums)
        result = [[]]

        for num in nums:
            cur_res = [val for val in result]
            for cur in cur_res:
                result += [cur + [num]]
        return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    sln = Solution()
    print(sln.subsets(nums=nums))
