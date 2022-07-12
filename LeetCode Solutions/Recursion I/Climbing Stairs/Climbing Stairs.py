class Solution:
    def climbStairs(self, n: int) -> int:
        num = 0
        num1 = 1
        for i in range(n):
            num2 = num + num1
            num = num1
            num1 = num2
        return (num1)