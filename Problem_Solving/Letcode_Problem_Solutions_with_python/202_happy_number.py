class Solution:
    def isHappy(self, n: int) -> bool:
        occured = []
        while n != 1:
            s = 0
            for i in str(n):
                s = s + int(i) * int(i)
            n = s

            if n in occured:
                return False

            occured.append(n)
        return True


if __name__ == "__main__":
    n = 7
    s = Solution().isHappy(n)
    print(s)
