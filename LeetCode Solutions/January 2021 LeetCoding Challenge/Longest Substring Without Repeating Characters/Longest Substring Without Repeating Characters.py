class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, length = 0, 0, 0
        Hashset = set()
        while (i < len(s) and j < len(s)):
            if (s[j] not in Hashset):
                Hashset.add(s[j])
                length = max(length, j-i+1)
                j += 1
            else:
                Hashset.remove(s[i])
                i += 1
        return length