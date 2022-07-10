class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        wordset, former = set(['']), ''
        for word in words:
            if word[:-1] in wordset:
                former = word if len(word)>len(former) else former
                wordset.add(word)
        return former