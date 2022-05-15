from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        mn = min(salary)
        mx = max(salary)
        salary.remove(mn)
        salary.remove(mx)
        avg = sum(salary)/len(salary)
        return avg


if __name__ == "__main__":
    salary = [4000, 3000, 1000, 2000]
    s = Solution().average(salary)
    print(s)
