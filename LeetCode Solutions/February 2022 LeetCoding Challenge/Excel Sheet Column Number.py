class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        r = 0
        for i in range(len(columnTitle)):
            r += (ord(columnTitle[len(columnTitle) - i - 1]) - 64)*26**i
        return r