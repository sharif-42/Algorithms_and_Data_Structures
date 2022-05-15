class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        l = len(arr)
        total = 0

        for i in range(1, l + 1, 2):
            for j in range(l):
                if j + i <= l:
                    total += sum(arr[j:j + i])
        return total


if __name__ == "__main__":
    arr = [10,11,12]
    s = Solution().sumOddLengthSubarrays(arr)
    print(s)
