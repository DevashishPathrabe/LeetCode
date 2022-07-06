class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        for bit in target:
            if (ord(bit) - ord('0')) - flips%2 != 0:
                flips += 1
        return flips