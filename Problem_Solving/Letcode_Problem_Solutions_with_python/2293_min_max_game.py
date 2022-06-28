class Solution:
    def minMaxGame(self, nums) -> int:
        new_nums = []
        count = 0
        if len(nums) == 1:
            return nums[0]

        for i in range(0, len(nums), 2):
            if count % 2:
                new_nums.append(max(nums[i], nums[i + 1]))
            else:
                new_nums.append(min(nums[i], nums[i + 1]))
            count+=1
        return self.minMaxGame(nums=new_nums)


if __name__ == "__main__":
    nums = [10, 10,1,5,4,2, 100, 100]
    solution = Solution().minMaxGame(nums=nums)
    print(solution)
