class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ag = sum(nums[:k])
        maximum = ag
        for i in range(len(nums)-k):
            ag = ag - nums[i]+nums[i+k]
            maximum = max(maximum, ag)
        return maximum/k