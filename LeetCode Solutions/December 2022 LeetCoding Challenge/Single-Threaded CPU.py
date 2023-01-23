class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([t + [i] for i, t in enumerate(tasks)])
        heap, ans = [], []
        last_enq = 0
        for enq, pro, idx in tasks:
            while heap and last_enq < enq:
                p, i, e = heapq.heappop(heap)
                last_enq = max(e, last_enq) + p
                ans.append(i)
            heapq.heappush(heap, (pro, idx, enq))
        while heap:
            _, i, _ = heapq.heappop(heap)
            ans.append(i)
        return ansclass Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        def helper(p, visited, paths):
            visited.append(p)
            if p == N-1:
                paths.append([item for item in visited])
            else:
                for nei in graph[p]:            
                    helper(nei, visited, paths)
            visited.pop()
        visited, paths = [], []
        helper(0, visited, paths)
        return paths