class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c, d = Counter(s), Counter(t)
        overlapping_Chars = sum((c&d).values())
        return len(s) - overlapping_Chars