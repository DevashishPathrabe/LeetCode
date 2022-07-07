class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = 10**4
        for i, n in enumerate(nums):
            if n == target:
                if abs(i-start) < result:
                    result = abs(i - start)
        return result