class Solution:
    def numSplits(self, s: str) -> int:
        first = {}
        last = {}
        for i, w in enumerate(s):
            if w not in first:
                first[w] = i
            last[w] = i
        indices = list(first.values()) + list(last.values())
        indices.sort()
        m = len(indices)//2
        return indices[m] - indices[m-1]