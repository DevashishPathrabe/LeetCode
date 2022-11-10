class Solution:
    def oddString(self, words: List[str]) -> str:
        def calculateDifference(word: str) -> tuple:
            return tuple(ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1))
        differenceDict = collections.defaultdict(int)
        for word in words:
            differenceDict[calculateDifference(word)] += 1
        for word in words:
            if differenceDict[calculateDifference(word)] == 1:
                return word