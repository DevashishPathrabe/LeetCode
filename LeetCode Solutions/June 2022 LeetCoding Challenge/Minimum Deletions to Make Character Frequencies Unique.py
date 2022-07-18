class Solution:
    def minDeletions(self, s: str) -> int:
        counts = collections.Counter(s)
        freq, result = set(), 0
        for i, j in counts.items():
            while j > 0 and j in freq:
                j -= 1
                result += 1
            freq.add(j)
        return result