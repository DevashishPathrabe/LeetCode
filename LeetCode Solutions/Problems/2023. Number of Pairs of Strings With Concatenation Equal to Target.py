class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a, b = nums[i], nums[j]
                if a+b == target:
                    result += 1
                if b+a == target:
                    result += 1
        return result