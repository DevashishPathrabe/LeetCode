class Solution:
    def baseNeg2(self, n: int) -> str:
        s = ''
        if n == 0:
            return '0'
        while n != 0:
            if n % 2 != 0:
                s = '1' + s
                n = (n - 1) // -2
            else:
                s = '0' + s
                n //= -2
        return s