import copy


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy_of_nums = copy.deepcopy(nums)
        for val in copy_of_nums:
            if val == 0:
                nums.remove(val)
                nums.append(val)
        return nums


if __name__ == "__main__":
    arr = [0]
    s = Solution().moveZeroes(arr)
    print(s)
