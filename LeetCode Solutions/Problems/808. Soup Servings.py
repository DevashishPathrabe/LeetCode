class Solution:
    def soupServings(self, n: int) -> float:
        n = math.ceil(n / 25)
        if n >= 200:
            return 1
        dp = [[1] * (n + 1) for _ in range(n+1)]
        dp[0][0] = 0.5
        for i in range(1, n+1):
            dp[i][0] = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                m = lambda x: max(0, x)
                dp[i][j] = (dp[m(i-4)][j] + dp[m(i-3)][j-1] + dp[m(i-2)][m(j-2)] + dp[i-1][m(j-3)]) / 4
                if 1 - dp[i][j] < 1e-6:
                    break
            if 1 - dp[i][i] < 1e-6:
                break
        return dp[n][n]