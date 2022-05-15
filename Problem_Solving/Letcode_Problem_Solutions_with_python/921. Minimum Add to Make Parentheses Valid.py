class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if len(S)==0:
            return 0

        stack = []
        for i in S:
            if stack:
                top = stack[-1]
                if i==')' and top=='(':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)


if __name__=='__main__':
    sln = Solution()
    s = ')))()()()((('
    sln = sln.minAddToMakeValid(s)
    print(sln)