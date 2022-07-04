class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp, n, maximum = [0] * len(arr), len(arr), 0
        for i in range(n):
            if i < k:
                if maximum < arr[i]:
                    maximum = arr[i]
                dp[i] = maximum * (i+1)
            else:
                maximum = 0
                for j in range(1, k+1):
                    if maximum < arr[i-j+1]:
                        maximum = arr[i-j+1]
                    temp = dp[i-j] + maximum * j
                    if dp[i] < temp:
                        dp[i] = temp
        return dp[-1]