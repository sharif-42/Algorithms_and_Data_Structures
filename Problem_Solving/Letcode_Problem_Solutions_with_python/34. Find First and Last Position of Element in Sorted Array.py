class Solution:
    def binary_search(self, nums, target):
        beg = 0
        end = len(nums) - 1
        mid = 0
        while beg <= end:
            mid = (beg + end) // 2
            if nums[mid] == target:
                return True, mid

            if target < nums[mid]:
                end = mid - 1
            else:
                beg = mid + 1
        else:
            return False, mid

    def searchRange(self, nums, target: int):
        is_found, index = self.binary_search(nums=nums, target=target)
