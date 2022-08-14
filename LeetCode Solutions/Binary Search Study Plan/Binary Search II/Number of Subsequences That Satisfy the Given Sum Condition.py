class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        i, j = 0, n-1
        result = 0 
        NUM = 10**9+7
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] <= target:
                result += pow(2, j-i, NUM)
                i += 1
        return result % NUM