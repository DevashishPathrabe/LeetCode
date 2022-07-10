class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        HammingDistance = 0
        n = len(nums)
        for i in range(32):
            ones = 0
            for num in nums:
                ones += (num>>i)&1
            HammingDistance += ones*(n-ones)
        return HammingDistance