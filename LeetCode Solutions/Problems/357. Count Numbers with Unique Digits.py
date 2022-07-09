class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        result, k, m = 1, 9, 9
        for i in range(n):
            result += m
            m *= (k - i)
        return result