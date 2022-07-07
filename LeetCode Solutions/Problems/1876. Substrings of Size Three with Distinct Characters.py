class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        return sum(3 == len(set(s[i:i+3])) for i in range(len(s) - 2))