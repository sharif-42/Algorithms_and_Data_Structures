class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_count = 0
        if sorted(s1) != sorted(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_count += 1
        return diff_count <= 2


if __name__ == "__main__":
    s1 = "kelb"
    s2 = "kelb"
    s = Solution().areAlmostEqual(s1, s2)
    print(s)
