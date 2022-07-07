class Solution:
    def makeFancyString(self, s: str) -> str:
        d = s[:2]
        for i in range(2, len(s)) :
            if  d[-1] != s[i] or d[-2] != s[i] :
                d += s[i]   
        return d