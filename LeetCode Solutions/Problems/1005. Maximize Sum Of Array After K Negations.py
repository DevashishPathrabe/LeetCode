class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while k:
            nums[nums.index(min(nums))] =- min(nums)
            k -= 1
        return sum(nums)