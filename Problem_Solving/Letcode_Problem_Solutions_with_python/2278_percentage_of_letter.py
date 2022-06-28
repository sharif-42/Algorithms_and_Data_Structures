import math


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for i in s:
            if i == letter:
                count += 1
        count = count / len(s)
        return math.floor(count * 100)


if __name__ == "__main__":
    s = "ssawtb"
    letter = "s"
    solution = Solution().percentageLetter(s=s, letter=letter)
    print(solution)
