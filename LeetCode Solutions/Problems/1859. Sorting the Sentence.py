class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        for i in s.split():
            d[i[-1]] = i[:-1]
        return ' '.join(d[k] for k in sorted(d))