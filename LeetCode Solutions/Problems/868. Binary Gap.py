class Solution:
    def binaryGap(self, n: int) -> int:
        longestDistance, flag, distance = 0, 0, 0
        while (n != 0):
            t = n % 2
            n //= 2
            if t == 1 and flag == 1:
                distance += 1
                longestDistance = max(longestDistance, distance)
                distance = 0
            elif t == 1 and flag == 0:
                flag = 1
            elif t == 0 and flag == 1:
                distance += 1
        return longestDistance