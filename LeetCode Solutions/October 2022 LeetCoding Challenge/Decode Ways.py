class Solution:
    def numDecodings(self, s: str) -> int:
        if (not s or s[0] == '0'):
            return 0
        sl = numberOfWays = 1
        if (s[0] == '0'):
            l = 0
        else:
            l = 1
        for i in range(1, len(s)):
            numberOfWays = 0
            if (s[i] != '0'):
                numberOfWays = l   
            twoDigit = int(s[i - 1: i + 1])
            if (twoDigit >= 10 and twoDigit <= 26):
                numberOfWays += sl
            sl, l = l, numberOfWays
        return numberOfWays