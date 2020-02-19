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

    def searchInsert(self, nums, target):
        if target == 0 or len(nums)==0:
            return 0
        is_found, index = self.binary_search(nums=nums, target=target)
        print(is_found, index)
        if is_found:
            return index
        else:
            if nums[index]<target:
                return index+1
            return index


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 10
    sln = Solution().searchInsert(nums, target)
    print(sln)
