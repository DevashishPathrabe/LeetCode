class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        m = 0
        for i in primes:
            if i <= n:
                m += 1
        return (math.factorial(m) * math.factorial(n - m)) % (10**9 + 7)