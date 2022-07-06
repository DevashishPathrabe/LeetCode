class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        result = 0
        n = len(s)
        def helper(index, current, visited):
            nonlocal result, n
            if (index == n):
                result = max(result, current)
                return
            for i in range(index, n):
                if (s[index:i+1] not in visited):
                    helper(i+1, current+1, visited + (s[index:i+1],))
        helper(0, 0, ())
        return result