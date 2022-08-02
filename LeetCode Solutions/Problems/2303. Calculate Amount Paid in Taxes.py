class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax, lower = 0, 0
        for upper, percent in brackets:
            if lower > income:
                break
            tax += (min(upper, income) - lower) * percent
            lower = upper
        return tax / 100