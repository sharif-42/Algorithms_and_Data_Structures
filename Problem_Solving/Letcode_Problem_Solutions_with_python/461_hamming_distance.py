class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        while x or y:
            print(x, bin(x), y, bin(y))
            if x & 1 ^ y & 1:
                cnt += 1
            x >>= 1
            y >>= 1
        return cnt


if __name__ == "__main__":
    ans = Solution().hammingDistance(5,4)
    print(ans)
