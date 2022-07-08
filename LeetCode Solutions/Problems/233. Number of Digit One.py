class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        count = 0
        i = 1
        while i * 10 <= n:
            i *= 10
        count += min(2 * i - 1, n) - i + 1
        count +=  (n // i) * self.countDigitOne(i - 1) + self.countDigitOne(n % i)
        return count