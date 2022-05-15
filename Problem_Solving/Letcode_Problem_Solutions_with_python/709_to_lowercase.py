class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


if __name__ == "__main__":
    s =  "HeMKlo"
    s = Solution().toLowerCase(s=s)
    print(s)
