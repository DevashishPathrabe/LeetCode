class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        wordsSet = set(words)
        for word in words:
            if (word in wordsSet):
                for i in range(1,len(word)):
                    wordsSet.discard(word[i:])
        return len("#".join(list(wordsSet))) + 1