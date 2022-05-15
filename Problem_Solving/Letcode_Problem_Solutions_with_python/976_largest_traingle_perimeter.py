class Solution:
    def largestPerimeter(self, nums) -> int:
        nums.sort()
        m = len(nums)
        while m > 2:
            if nums[m-3] + nums[m-2] > nums[m-1]:
                return nums[m-1] + nums[m-2] + nums[m-3]
            else:
                m -= 1
        return 0


if __name__ == "__main__":
    l = [3,6,2,3]
    s = Solution().largestPerimeter(l)
    print(s)
