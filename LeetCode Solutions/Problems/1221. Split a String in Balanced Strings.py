class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result, count = 0, 0
        for i in range(len(s)):
            if s[i] == 'L':
                count -= 1
            else:
                count += 1
            if count == 0:
                result += 1
        return result