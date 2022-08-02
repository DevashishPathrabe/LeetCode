class Solution:
    def greatestLetter(self, s: str) -> str:
        s = sorted(s)
        for i in reversed(range(len(s))): 
            if s[i].upper() in s and s[i].lower() in s:
                return s[i].upper()
        return ""