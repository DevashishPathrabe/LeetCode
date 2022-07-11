class Solution:
    def reorganizeString(self, s: str) -> str:
        count = collections.Counter(s)
        heap = []
        for key in count:
            if count[key] > ((len(s) + 1) // 2):
                return ""
            heapq.heappush(heap, (-count[key], key))
        result = ""
        while heap:
            first = heapq.heappop(heap)
            if len(heap) == 0:
                return result + first[1]
            second = heapq.heappop(heap)
            result += first[1]
            result += second[1]
            if first[0] + 1 != 0:
                heapq.heappush(heap, (first[0] + 1, first[1]))
            if second[0] + 1 != 0:
                heapq.heappush(heap, (second[0] + 1, second[1]))
        return result