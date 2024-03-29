class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        i = 0
        s1, s2 = min(strs), max(strs)
        while (i < len(s1) and i < len(s2) and s1[i] == s2[i]):
            i += 1
        return s1[:i]