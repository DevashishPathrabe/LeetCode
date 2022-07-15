class Solution:
    def firstUniqChar(self, s: str) -> int:
        if (not s): 
            return -1
        if (len(s) == 1):
            return 0
        for i, ch in enumerate(s):
            if (ch not in s[:i] + s[i+1:]):
                return i
        return -1