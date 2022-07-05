class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for word1 in words:
            for word2 in words:
                if word1 != word2 and word1 in word2:
                    result.add(word1)
        return result