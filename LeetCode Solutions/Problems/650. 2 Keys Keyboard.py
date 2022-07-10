class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if n <= 5:
            return n
        for i in range(n//2, -1, -1):
            if n % i == 0:
                return self.minSteps(i) + (n // i)