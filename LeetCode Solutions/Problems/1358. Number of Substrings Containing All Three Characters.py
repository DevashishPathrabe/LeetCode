class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n, d = 0, {'a': -1, 'b': -1, 'c': -1}
        for i, c in enumerate(s):
            d[c] = i
            n += i - min(d.values())
        return (1 + len(s)) * len(s) // 2 - n