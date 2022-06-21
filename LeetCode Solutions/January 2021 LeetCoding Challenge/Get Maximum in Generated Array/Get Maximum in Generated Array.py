class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if (n <= 1):
            return  n
        maxInteger = [0] * (n + 1)
        maxInteger[1] = 1
        for i in range(1, (n + 1) // 2):
            maxInteger[i * 2] = maxInteger[i]
            maxInteger[(i * 2) + 1 ] = maxInteger[i] + maxInteger[i +1]
        return max(maxInteger)