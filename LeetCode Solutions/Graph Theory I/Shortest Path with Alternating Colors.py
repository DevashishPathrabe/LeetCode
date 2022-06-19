class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = {x : {-1:[],1:[]} for x in range(n)}
        for edge in redEdges:
            graph[edge[0]][-1].append(edge[1])
        for edge in blueEdges:
            graph[edge[0]][1].append(edge[1])
        distances = { -1: [inf]*n , 1 : [inf] * n }
        q = deque()
        q.append((0,-1,0))
        q.append((0,1,0))
        while q:
            src, color, dist = q.popleft()
            if distances[color][src] >= dist:
                distances[color][src] = dist
                for nei in graph[src][-color]:
                    q.append((nei,-color,dist+1))
        return [min(rd,bd) if min(rd,bd) != inf else -1 for rd,bd in zip(distances[-1],distances[1])]