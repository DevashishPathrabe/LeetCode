class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        sentences = []
        def helper(i, string):
            if i == len(s):
                sentences.append(string[:-1])
            for j in range(i, len(s)+1):
                if s[i:j] in wordDict:
                    helper(j, string + s[i:j] + " ")
        helper(0, "")
        return sentences