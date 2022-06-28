from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        res.append(list(nums1-nums2))
        res.append(list(nums2-nums1))
        return res


if __name__ == "__main__":
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    res = Solution().findDifference(nums1=nums1, nums2=nums2)
    print(res)