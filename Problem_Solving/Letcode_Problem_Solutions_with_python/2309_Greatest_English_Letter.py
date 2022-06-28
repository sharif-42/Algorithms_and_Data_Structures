class Solution:
    def greatestLetter(self, s: str) -> str:
        new_s = []
        for i in range(len(s)):

            if s[i].isupper() and s[i].lower() in s[i:]:
                new_s.append(s[i].upper())
            elif s[i].islower() and s[i].upper() in s[i:]:
                new_s.append(s[i].upper())
        if new_s:
            new_s = sorted(new_s)
            return new_s[-1]
        else:
            return ""


if __name__ == "__main__":
    s = "lEeTcOdE"
    solution = Solution().greatestLetter(s=s)
    print(solution)
