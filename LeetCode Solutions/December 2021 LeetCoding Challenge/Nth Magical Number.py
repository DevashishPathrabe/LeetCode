class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        low = 2
        high = 10**100
        while (low <= high):
            mid = (low + high) // 2
            if mid // a + mid // b - mid // ((a * b) // math.gcd(a, b)) >= n:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result % (10 ** 9 + 7)