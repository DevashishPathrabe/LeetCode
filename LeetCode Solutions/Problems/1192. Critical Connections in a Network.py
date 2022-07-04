class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edgeMap = defaultdict(list)
        for i, j in connections:
            edgeMap[i].append(j)
            edgeMap[j].append(i)
        disc, low, time, criticalConnections = [0] * n, [0] * n, [1], []
        def dfs(current: int, previous: int):
            disc[current] = low[current] = time[0]
            time[0] += 1
            for next in edgeMap[current]:
                if(not disc[next]):
                    dfs(next, current)
                    low[current] = min(low[current], low[next])
                elif(next != previous):
                    low[current] = min(low[current], disc[next])
                if(low[next] > disc[current]):
                    criticalConnections.append([current, next])
        dfs(0, -1)
        return criticalConnections