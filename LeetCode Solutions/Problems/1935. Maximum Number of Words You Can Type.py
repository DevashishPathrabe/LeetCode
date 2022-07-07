class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        lst = list(map(str,text.split()))
        k = len(lst)
        if len(brokenLetters) == 0:
            return k
        for x in lst:
            for text in x:
                tmp = 0
                for m in brokenLetters:
                    if text == m:
                        tmp = 1
                        break
                if tmp == 1:
                    k -= 1
                    break
        return k;