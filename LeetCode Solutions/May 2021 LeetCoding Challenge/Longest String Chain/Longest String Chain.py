class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        W = [set() for _ in range(17)]
        for word in words:
            W[len(word)].add(word)
        arr, longestPossibleLength = defaultdict(lambda:1), 1
        for i in range(16, 0, -1):
            if (len(W[i-1]) == 0):
                continue
            for word in W[i]:
                wordValue = arr[word]
                for j in range(len(word)):
                    predecessors = word[0:j] + word[j+1:]
                    if (predecessors in W[i-1] and wordValue >= (arr.get(predecessors) or 1)):
                        arr[predecessors]= wordValue + 1
                        longestPossibleLength = max(longestPossibleLength, wordValue+1)
        return longestPossibleLength