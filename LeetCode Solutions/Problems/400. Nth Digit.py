class Solution:
    def findNthDigit(self, n: int) -> int:
        d, base = 1, 0
        while n > 9 * 10 ** (d-1) * d + base:
            base += 9 * 10 ** (d-1) * d
            d += 1
        number = (10 ** (d-1) - 1) + (n-base) // d
        number = int(number)
        remainder = (n-base) % d
        if remainder == 0:
            return int(str(number)[-1])
        else:
            return int(str(number+1)[remainder-1])