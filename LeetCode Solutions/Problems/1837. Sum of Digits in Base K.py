class Solution:
    def sumBase(self, n: int, k: int) -> int:
        c = 0
        while n > 0:
            c += n % k
            n = n // k
        return c