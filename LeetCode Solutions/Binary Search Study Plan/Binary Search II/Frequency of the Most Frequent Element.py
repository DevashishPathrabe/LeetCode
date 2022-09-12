class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ans = 1
        nums=sorted(nums)
        sums = 0
        l = 0
        for r in range(len(nums)):
            sums += nums[r]
            while l < r and sums + k <  nums[r] * (r - l + 1):
                sums -= nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans