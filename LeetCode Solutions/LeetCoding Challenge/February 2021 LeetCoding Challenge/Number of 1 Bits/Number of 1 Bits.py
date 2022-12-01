class Solution:
    def hammingWeight(self, n: int) -> int:
        numberOf1bits = 0
        while (n):
            numberOf1bits += n%2
            n = n>>1
        return numberOf1bits