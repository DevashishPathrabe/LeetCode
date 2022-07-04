class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        stones = [s*-1 for s in stones]
        heapq.heapify(stones)
        while (len(stones) > 1):
            y = -1 * heapq.heappop(stones)
            x = -1 * heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -1*(y-x))
        if len(stones):
            return -1 * heapq.heappop(stones)
        else:
            return 0