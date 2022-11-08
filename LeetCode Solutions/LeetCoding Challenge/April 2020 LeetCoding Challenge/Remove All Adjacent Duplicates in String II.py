class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count, i = 1, 1
        while(i < len(s)):
            if(s[i] == s[i-1]):
                count += 1
            else:
                count = 1
            if(count == k):
                s = self.removeDuplicates(s[:i-k+1] + s[i+1:], k)
            i += 1
        return s