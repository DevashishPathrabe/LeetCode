class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        int MOD = 1000_000_000 + 7;
		int[][] dp = new int[n + 1][target + 1];
		dp[0][0] = 1;
		for (int i=1; i<=n; i++){
			for (int j=1; j<=target; j++){
				if (j > i * k){
					dp[i][j] = dp[i - 1][j - 1];
				} else {
					for (int l=1; l<=k && l<=j; l++){
						dp[i][j] = (dp[i][j] % MOD + dp[i - 1][j - l] % MOD) % MOD;
					}
				}
			}
		}
		return dp[n][target];
    }
}