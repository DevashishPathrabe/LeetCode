class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = set()
        start = 0
        for end in range(1, len(nums)):
            if nums[end] - nums[start] == k:
                result.add((nums[start], nums[end]))
            while nums[end] - nums[start] > k and start < end:
                start += 1
                if  nums[end] - nums[start] == k and start < end:
                    result.add((nums[start], nums[end]))
        return len(result)