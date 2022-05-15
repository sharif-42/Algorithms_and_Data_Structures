class Solution:
    def maximumWealth(self, accounts) -> int:
        max_wealth = 0
        for i in accounts:
            s = sum(i)
            if s > max_wealth:
                max_wealth = s
        return max_wealth


if __name__ == "__main__":
    arr = [[2,8,7],[7,1,3],[1,9,5]]
    s = Solution().maximumWealth(arr)
    print(s)
