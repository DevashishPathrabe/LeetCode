class Solution:
    def countOrders(self, n: int) -> int:
        result = 1
        p = 10**9+7
        for i in range(1, n+1):
            result *= i * (2*i - 1)
            result = result % p
        return result