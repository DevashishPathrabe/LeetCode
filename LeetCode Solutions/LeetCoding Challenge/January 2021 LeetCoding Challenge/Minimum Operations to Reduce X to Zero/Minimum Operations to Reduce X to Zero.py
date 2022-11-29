class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums)-x
        if (target < 0):
            return -1
        if (target == 0):
            return len(nums)
        left ,currentSum ,minNumberOfOperations = 0, 0, -1
        for i in range(len(nums)):
            if (currentSum < target):
                currentSum += nums[i]
            while (currentSum >= target):
                if (currentSum == target):
                    minNumberOfOperations = max(minNumberOfOperations, i-left+1)
                currentSum -= nums[left]
                left += 1
        if (minNumberOfOperations != -1):
            return len(nums) - minNumberOfOperations 
        else:
            return -1