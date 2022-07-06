class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1
        obj = {}
        for i in range(0, len(s)):
            if s[i] in obj:
                result = max(result, abs(i - obj[s[i]] - 1))
            else:
                obj[s[i]] = i
        return result