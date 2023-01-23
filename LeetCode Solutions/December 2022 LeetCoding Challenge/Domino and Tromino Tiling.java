class Solution {
    public int numTilings(int n) {
        if (n == 1){
            return 1;
        }
        int[] dp = new int[n];
        dp[0] = 1;
        dp[1] = 2;
        int[] dpa = new int[n];
        dpa[1] = 1;
        for (int i=2; i<n; i++){
            dp[i] = ((dp[i - 1] + dp[i - 2]) % 1000000007 + (dpa[i - 1] * 2) % 1000000007) % 1000000007;
            dpa[i] = (dp[i - 2] + dpa[i - 1]) % 1000000007;
        }
        return dp[n - 1];
    }
}