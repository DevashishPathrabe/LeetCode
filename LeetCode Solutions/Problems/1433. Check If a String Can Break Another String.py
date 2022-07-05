class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2=sorted(s2)
        g = True
        for i in range(len(s2)):
            if s1[i] > s2[i]:
                g = False
        if g == True:
            return True
        else:
            for i in range(len(s1)):
                if s1[i] < s2[i]:
                    return False
            return True