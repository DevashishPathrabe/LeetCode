class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = pow(10, 9) + 7
        if n == 1:
            return 5
        if n % 2 == 0:
            return (pow(5, n//2, mod) * pow(4, n//2, mod)) % mod
        if n % 2 == 1:
            return (pow(5, n//2 + 1, mod) * pow(4, n//2, mod)) % mod