import math


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        count = 0
        if high % 2 and low % 2:
            count = diff // 2 + 1
        elif high % 2 == 0 and low % 2 == 0:
            count = diff // 2
        else:
            count = diff // 2 + 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countOdds(2, 5))
