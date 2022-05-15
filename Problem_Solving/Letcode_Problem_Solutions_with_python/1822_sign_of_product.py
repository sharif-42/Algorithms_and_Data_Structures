class Solution:
    def arraySign(self, nums) -> int:
        neg_cnt = 0
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                neg_cnt += 1
        if neg_cnt % 2:
            return -1
        else:
            return 1


if __name__ == "__main__":
    nums =  [-1,1,-1,1,-1]

    s = Solution().arraySign(nums)
    print(s)
