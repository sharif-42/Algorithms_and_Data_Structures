class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxlen, n = 0, len(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxlen = max(maxlen, i - stack[-1])
            print(i, maxlen, stack)
        return maxlen


if __name__ == '__main__':
    sln = Solution()
    s = "()())()()"
    sln = sln.longestValidParentheses(s)
    print(sln)
