class Solution:
    def averageValue(self, nums: List[int]) -> int:
        result, count = 0, 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] % 3 == 0:
                result += nums[i]
                count += 1
        if count != 0:
            return result//count
        return 0