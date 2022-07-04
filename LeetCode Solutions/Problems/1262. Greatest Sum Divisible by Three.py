class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        maxSum = r1 = r2 = 0
        for num in nums:
            candidates = num + maxSum, num + r1, num + r2
            for candidate in candidates:
                if candidate % 3 == 0:
                    maxSum = max(maxSum, candidate)
                elif candidate % 3 == 1:
                    r1 = max(r1, candidate)
                elif candidate % 3 == 2:
                    r2 = max(r2, candidate)
        return maxSum