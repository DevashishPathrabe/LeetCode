class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sList = list(filter(None, s.split(' ')))
        if(len(sList) == 0):
            return 0
        else:
            return len(sList[-1])