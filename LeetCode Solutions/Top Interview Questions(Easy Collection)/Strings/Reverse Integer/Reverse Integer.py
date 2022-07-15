class Solution:
    def reverse(self, x: int) -> int:
        signed = (x > 0) - (x < 0)
        reverse = int(str(x*signed)[::-1])
        if (signed*reverse < -2**31 or signed*reverse > 2**31 - 1):
            return 0
        else:
            return signed * reverse