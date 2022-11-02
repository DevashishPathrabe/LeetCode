class Solution:
    def climbStairs(self, n: int) -> int:
        num1, num2 = 0, 1
        for i in range(n):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        return num3