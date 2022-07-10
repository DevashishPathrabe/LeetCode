class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, n = 0, len(bits)
        while i < n-1:
            i += bits[i] + 1
        return n - i == 1