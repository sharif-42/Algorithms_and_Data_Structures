class Solution:
    def calculateTax(self, brackets, income: int) -> float:
        totaltax = prevbracket = 0
        for upper, percent in brackets:
            if income >= upper:
                totaltax += (upper - prevbracket) * percent / 100
                prevbracket = upper
            else:
                totaltax += (income - prevbracket) * percent / 100
                return totaltax
        return totaltax


if __name__ == "__main__":
    brackets = [[2, 7], [3, 17], [4, 37], [7, 6], [9, 83], [16, 67], [19, 29]]
    income = 18
    # income = 2
    solution = Solution().calculateTax(brackets, income)
    print(solution)
