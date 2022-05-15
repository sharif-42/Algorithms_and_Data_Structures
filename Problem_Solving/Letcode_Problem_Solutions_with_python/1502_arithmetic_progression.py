class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        arr = sorted(arr)
        arr_length = len(arr)
        ans = set()
        for i in range(1, arr_length):
            ans.add(arr[i] - arr[i - 1])
        if len(ans) == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    nums = [1,2,4]

    s = Solution().canMakeArithmeticProgression(nums)
    print(s)
