class Solution:
    def countAsterisks(self, s: str):
        star_count = 0
        arr = s.split('|')
        for i in range(len(arr)):
            count = 0
            if i % 2 == 0:
                count = arr[i].count('*')
                star_count += count
        return star_count


if __name__ == "__main__":
    s = "iamprogrammer"
    solution = Solution().countAsterisks(s=s)
    print(solution)
