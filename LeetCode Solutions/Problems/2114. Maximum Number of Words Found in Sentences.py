class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximumNumberOfWords = 0
        for i in sentences:
            maximumNumberOfWords = max(maximumNumberOfWords, i.count(" ") + 1)
        return maximumNumberOfWords