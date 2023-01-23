class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)
        for _ in range(k):
            current = -heapq.heappop(heap)
            heapq.heappush(heap, -(current-current//2))
        return -sum(heap)