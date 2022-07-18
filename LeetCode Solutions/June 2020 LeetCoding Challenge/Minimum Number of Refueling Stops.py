class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        priorityQ = []
        leastNumber, i = 0, 0
        while(startFuel < target):
            while(i < len(stations) and stations[i][0] <= startFuel):
                heapq.heappush(priorityQ, -stations[i][1])
                i += 1
            if(not priorityQ):
                return -1
            startFuel += -heapq.heappop(priorityQ)
            leastNumber += 1
        return leastNumber