class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        minimumTime = totalPlant = 0
        for grow, currentPlant in reversed(sorted(zip(growTime, plantTime))):
            totalPlant += currentPlant
            minimumTime = max(minimumTime, totalPlant + grow)
        return minimumTime