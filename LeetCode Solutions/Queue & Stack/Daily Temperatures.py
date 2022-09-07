class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        daysCount = len(T)
        nextWarmDay = [0 for i in range(daysCount)]
        for i in range(daysCount-2, -1, -1):
            nextDay = 1
            while nextDay and T[i + nextDay] <= T[i]:
                if(nextWarmDay[i + nextDay]):
                    nextDay += nextWarmDay[i + nextDay]
                else:
                    nextDay = 0
            nextWarmDay[i] = nextDay
        return nextWarmDay