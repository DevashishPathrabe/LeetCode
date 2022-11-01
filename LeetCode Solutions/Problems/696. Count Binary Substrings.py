class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        current, previous, result = 1, 0, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current += 1
            else:
                result += min(current, previous)
                previous, current = current, 1
        return result + min(current, previous)