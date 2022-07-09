class Solution:
    def toHex(self, num: int) -> str:
        hex = "0123456789abcdef"
        result = ""
        if num == 0:
            return "0"
        if num < 0:
            num += 2**32
        while num:
            result = hex[num%16] + result
            num //= 16
        return result