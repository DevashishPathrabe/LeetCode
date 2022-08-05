class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        i = 0
        for i in range(len(nums)):
            if (i == nums.index(m)):
                continue
            if (2 * nums[i] > m):
                return -1
        return nums.index(m)