class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def helper(word):
            dict = {}
            for i in word:
                if(i not in dict):
                    dict[i] = 1
                else:
                    dict[i] += 1
            return sorted(dict.values())
        return helper(word1) == helper(word2) and set(word1) == set(word2)