class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a = len(text1)
        b = len(text2)
        dp = [[-1] * (b + 1) for i in range(a + 1)]
        for i in range(a + 1):
            for j in range(b + 1):
                if (i == 0 or j == 0):
                    dp[i][j] = 0
                elif (text1[i - 1] == text2[j - 1]):
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1],dp[i - 1][j])
        return dp[a][b]