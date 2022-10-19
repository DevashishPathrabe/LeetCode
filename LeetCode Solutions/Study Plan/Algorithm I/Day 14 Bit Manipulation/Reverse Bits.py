class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            if (n&1):
                result += 1 << (31-i)
            n >>= 1
        return result