class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            count1 = num.count(str(i))
            if count1 != int(num[i]):
                return False
        return True


if __name__ == "__main__":
    num = "030"
    print(num)
    solution = Solution().digitCount(num=num)
    print(solution)
