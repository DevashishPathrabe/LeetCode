class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s = list(s)
        x = len(s)
        if x <= 1 or s == s[::-1]:
            return "".join(s)
        for j in range(0, x):
            s.insert(j, s[x-1])
            if s == s[::-1]:
                return "".join(s)