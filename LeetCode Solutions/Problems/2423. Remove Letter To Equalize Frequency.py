class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            s = word[:i] + word[i+1:]
            c = Counter(s)
            if len(set(c.values())) == 1:
                return True
        return False