class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_string = word1 if len(word1) > len(word2) else word2
        min_string = word2 if len(word1) > len(word2) else word1
        merged_string = ""
        i = -1
        for i in range(len(min_string)):
            merged_string += word1[i] + word2[i]

        if i == -1:
            i = 0
            merged_string += max_string[i:]
        else:
            merged_string += max_string[i + 1:]
        return merged_string


if __name__ == "__main__":
    word1 = "f"
    word2 = "b"
    s = Solution().mergeAlternately(word1=word1, word2=word2)
    print(s)
