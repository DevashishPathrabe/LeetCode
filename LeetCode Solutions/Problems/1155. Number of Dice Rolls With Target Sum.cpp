class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        if (n > target || n * k < target) {
            return 0;
        }
        vector<vector<int>> dp(n+1, vector<int>(target+1, 0));
        int MOD = 1000000007;
        dp[0][0] = 1;
        for (int i=1; i<=n; i++) {
            for (int j=1; j<=target; j++) {
                dp[i][j] = (dp[i][j-1] + dp[i-1][j-1]) % MOD;
                if (j > k) {
                    dp[i][j] -= dp[i-1][j-k-1];
                    if (dp[i][j] < 0) {
                        dp[i][j] += MOD;
                    }
                }
            }
        }
        return dp[n][target];
    }
};