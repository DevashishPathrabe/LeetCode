class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daysCount = len(temperatures)
        nextWarmDay = [0 for i in range(daysCount)]
        for i in range(daysCount-2, -1, -1):
            nextDay = 1
            while(nextDay and temperatures[i + nextDay] <= temperatures[i]):
                if(nextWarmDay[i + nextDay]):
                    nextDay += nextWarmDay[i + nextDay]
                else:
                    nextDay = 0
            nextWarmDay[i] = nextDay
        return nextWarmDay