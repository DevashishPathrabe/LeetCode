class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        minimumTime = 0
        prev = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[prev]:
                if neededTime[prev] < neededTime[i]:
                    minimumTime += neededTime[prev]
                    prev = i
                else:
                    minimumTime += neededTime[i]
            else:
                prev = i
        return minimumTime