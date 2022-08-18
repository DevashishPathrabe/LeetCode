class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        l, r = 0, len(removable)
        while l < r:
            m = (l+r+1) // 2
            t = list(s)
            for i in removable[:m]:
                t[i] = ''
            iterator = iter(t)
            if all(c in iterator for c in p):
                l = m
            else:
                r = m - 1
        return l