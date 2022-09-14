class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1, sum2 = 0, 0
        for i in s:
            sum1 = sum1 + ord(i)
        for i in t:
            sum2 = sum2 + ord(i)
        return (chr(sum2 - sum1))