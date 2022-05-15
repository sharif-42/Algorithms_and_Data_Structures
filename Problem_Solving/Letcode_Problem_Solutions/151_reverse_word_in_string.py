class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()  # remove leading and trailing spaces

        new_word = ""
        list_of_words = []
        for i in s:
            if i == ' ':
                if not new_word=='':
                    list_of_words.insert(0, new_word)
                new_word = ""
            else:
                new_word += i
        if new_word:
            list_of_words.insert(0, new_word)

        new_word = ""
        for i in list_of_words:
            new_word = new_word + i + " "

        return new_word.strip()


if __name__ == "__main__":
    s = Solution()
    str = "a good   example"
    print(s.reverseWords(str))
