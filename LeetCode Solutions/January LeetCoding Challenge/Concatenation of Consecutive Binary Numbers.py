class Solution:
    def concatenatedBinary(self, n: int) -> int:
        decimalValue = ''
        for i in range(1, n+1):
            decimalValue += bin(i)[2:]
        return int(decimalValue, 2) % (10**9 + 7)