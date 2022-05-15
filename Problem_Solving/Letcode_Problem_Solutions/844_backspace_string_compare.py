import copy


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.remove_backspace(s)
        t = self.remove_backspace(t)
        # print(s,t)
        if s == t:
            return True
        else:
            return False

    def remove_backspace(self, string_data):
        string_array = string_data.split('#')
        # print("string_array", string_array)
        s = ''
        for i in string_data:
            if i == '#':
                s = s[:-1]
            else:
                s += i
        return s


if __name__ == "__main__":
    s1 = "a#c"
    s2 = "b"
    s = Solution().backspaceCompare(s1, s2)
    print(s)
