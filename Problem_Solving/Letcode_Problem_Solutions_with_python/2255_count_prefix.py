from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        counter = 0
        for i in words:
            if s.startswith(i):
                counter += 1
        return counter


if __name__ == "__main__":
    words = ["a", "b", "c", "ab", "bc", "abc"]
    s = "abc"
    res = Solution().countPrefixes(words=words, s=s)
    print(res)
