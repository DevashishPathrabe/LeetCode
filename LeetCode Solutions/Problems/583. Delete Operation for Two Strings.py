class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if(m < n):
            word1, word2, m, n = word2, word1, n, m
        dpLast, dpCurrent = [0] * (n + 1), [0] * (n + 1)
        for c1 in word1:
            for j in range(n):
                dpCurrent[j+1] = dpLast[j] + 1 if c1 == word2[j] else max(dpCurrent[j], dpLast[j+1])
            dpLast, dpCurrent = dpCurrent, dpLast
        return m + n - 2 * dpLast[n]