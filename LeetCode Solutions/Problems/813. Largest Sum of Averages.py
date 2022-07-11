class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        L = len(nums)
        S = [0]
        for x in nums:
            S.append(S[-1] + x)
        def average(i, N):
            return (S[N] - S[i]) / float(N - i)
        dp = [average(i, L) for i in range(L)]
        for _ in range(k - 1):
            for i in range(L):
                for j in range(i + 1, L):
                    dp[i] = max(dp[i], average(i, j) + dp[j])
        return dp[0]