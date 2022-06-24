class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        word = s.split(" ")
        if (len(word) != len(pattern)):
            return False
        for i in range(len(word)):
            if (pattern[i] not in d):
                if (word[i] not in d.values()):
                    d[pattern[i]] = word[i]
                else:
                    return False
            elif (d[pattern[i]] != word[i]):
                return False
        return True