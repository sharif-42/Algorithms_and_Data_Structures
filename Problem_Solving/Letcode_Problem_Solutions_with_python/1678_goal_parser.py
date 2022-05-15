class Solution:
    def interpret(self, command: str) -> str:
        result = ''
        prev = ''
        for i in command:
            if i == ')' and prev == '(':
                result += 'o'
            elif i == '(':
                prev = i
            elif i != ')':
                result += i
                prev = ''
        return result


if __name__ == "__main__":
    command = "(al)G(al)()()G"
    s = Solution().interpret(command=command)
    print(s)
