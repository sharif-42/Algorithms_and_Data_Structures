class Solution:

    def generateParenthesis(self, n: int):
        i = 0
        parenthesis = []
        s = ''
        for j in range(n):
            s += '()'
        parenthesis.append(s)

        while (n):
            s = ""
            additional_s = ""
            s += n * '('
            s += n * ')'
            additional_s += i * '('
            additional_s += i * ')'
            parenthesis.append(s+additional_s)
            # print(additional_s+s)
            i = i + 1
            n = n - 1
            print(i, n)
        return parenthesis


if __name__ == "__main__":
    n = 3
    solution = Solution().generateParenthesis(n)
    print(solution)
