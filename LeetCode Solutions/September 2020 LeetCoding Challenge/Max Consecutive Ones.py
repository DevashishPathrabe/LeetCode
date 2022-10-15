class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = count = 0
        nums.append(0)
        for i in nums:
            if i == 1:
                count += 1
            else:
                result = max(result, count)
                count = 0
        return result