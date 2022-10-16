class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        N, hs = len(buildings), []
        for i, (l, r, h) in enumerate(buildings):
            hs.append((l, 0, -h, i))
            hs.append((r, 1, h, i))
        hs.sort() 
        alive = [False] * N
        result, heap, current_height = [], [], 0
        for x, tp, h, i in hs: 
            if tp == 0:
                heapq.heappush(heap, (h, i))
                alive[i] = True
                if current_height < -h:
                    result.append([x, -h])
                    current_height = -h
            else:
                alive[i] = False
                while heap and not alive[heap[0][1]]:
                    heapq.heappop(heap)  
                if heap and -heap[0][0] < current_height:
                    current_height = -heap[0][0]
                    result.append([x, current_height])
                elif not heap:
                    current_height = 0 
                    result.append([x, current_height])
        return result