class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        x = (columnNumber-1) % 26
        result = (columnNumber-1) // 26
        if (result == 0):
            return digits[x]
        return self.convertToTitle(result) + digits[x]