class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        def getBulls(secret, guess):
            output = 0
            for i in range(len(secret)):
                if secret[i] == guess[i]:
                    output += 1
            return output
        def getCows(secret, guess):
            ns = ""
            ng = ""
            for i in range(len(secret)):
                if secret[i] != guess[i]:
                    ns += secret[i]
                    ng += guess[i]
            from collections import Counter
            c = c = list((Counter(list(ns)) & Counter(list(ng))).elements())
            return len(c)
        bulls = getBulls(secret, guess)
        cows = getCows(secret, guess)
        return "%dA%dB" % (bulls, cows)