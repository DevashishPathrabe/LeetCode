class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromePartitioning = []
        def helper(s, way):
            if(not s):
                return
            if(len(s) == 1):
                palindromePartitioning.append(way+[s])
                return
            for i in range(1, len(s)):
                if(s[:i] == s[:i][::-1]):
                    helper(s[i:], way+[s[:i]])
            if(s == s[::-1]):
                palindromePartitioning.append(way+[s])
            return
        helper(s, [])
        return palindromePartitioning