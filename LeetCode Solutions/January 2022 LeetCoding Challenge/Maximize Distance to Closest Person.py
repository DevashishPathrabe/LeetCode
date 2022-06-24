class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        leftIndex = -1
        maxDistance = 0
        for rightIndex, right in enumerate(seats):
            if right == 1:
                if leftIndex == -1:
                    maxDistance = rightIndex
                else:
                    maxDistance = max(maxDistance, (rightIndex - leftIndex) // 2)
                leftIndex = rightIndex
        if seats[-1] == 0:
            maxDistance = max(maxDistance, len(seats) - 1 - leftIndex)
        return maxDistance