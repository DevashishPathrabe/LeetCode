class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        L, D = len(s), collections.defaultdict(int)
        for j in range(L+1-minSize):
            D[s[j:j+minSize]] += (len(set(s[j:j+minSize])) <= maxLetters)
        return max(D.values())