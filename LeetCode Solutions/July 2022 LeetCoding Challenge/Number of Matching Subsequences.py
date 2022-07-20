class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        numberOfWords = 0
        for word, freq in Counter(words).items():
            index, match = 0, True
            for char in word:
                index = s.find(char, index) + 1
                if(not index):
                    match = False
                    break
            if(match):
                numberOfWords += freq
        return numberOfWords