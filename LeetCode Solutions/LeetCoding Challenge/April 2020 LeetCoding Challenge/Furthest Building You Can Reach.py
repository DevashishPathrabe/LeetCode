class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHeap = []
        n = len(heights)
        sumDifference = 0
        for i in range(1, n):
            difference = heights[i] - heights[i-1]
            if(difference > 0):
                heapq.heappush(maxHeap, -difference)
                sumDifference += difference
                if(sumDifference > bricks):
                    if(ladders == 0):
                        return i-1
                    ladders -= 1
                    maximum = -heapq.heappop(maxHeap)
                    sumDifference -= maximum
        return n - 1