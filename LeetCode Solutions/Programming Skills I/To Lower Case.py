class Solution:
    def toLowerCase(self, s: str) -> str:
        string = ""
        for c in s:
            n = ord(c)
            string += chr(n+32) if(n > 64) and (n < 91) else c
        return string