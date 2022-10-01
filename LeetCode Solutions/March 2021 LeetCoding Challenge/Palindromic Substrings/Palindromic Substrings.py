class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.helper(s, i, i)
            count += self.helper(s, i, i+1)
        return count
    def helper(self, s, left, right):
        count = 0
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
            count += 1
        return count