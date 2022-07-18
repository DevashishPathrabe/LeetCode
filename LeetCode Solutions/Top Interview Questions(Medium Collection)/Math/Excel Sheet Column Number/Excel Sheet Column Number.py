class Solution:
    def titleToNumber(self, s: str) -> int:
        r = 0
        for i in range(len(s)):
            r += (ord(s[len(s) - i - 1]) - 64) * 26**i
        return r