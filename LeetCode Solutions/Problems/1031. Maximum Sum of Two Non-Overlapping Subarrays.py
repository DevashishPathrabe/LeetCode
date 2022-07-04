class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        AL = [0]*len(nums)
        AM = [0]*len(nums)
        for i in range(len(nums)):
            if i >= firstLen-1:
                AL[i] = sum(nums[i-firstLen+1:i+1])
            if i >= secondLen-1:
                AM[i] = sum(nums[i-secondLen+1:i+1])
        dp = [[0 for _ in range(len(nums))] for _ in range(2)]
        max_val = 0
        for i in range(len(nums)):
            if i >= firstLen-1+secondLen:
                dp[0][i] = AM[i] + max(AL[0:i-secondLen+1])
                dp[1][i] = AL[i] + max(AM[0:i-firstLen+1])
                max_val = max(max_val, max(dp[0][i], dp[1][i]))
        return max_val