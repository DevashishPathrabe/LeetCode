class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads) == 1:
            return 1
        graph = defaultdict(set)
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)
        combs = combinations(range(n), 2)
        rank = 0
        for u, v in combs:
            rank = max(rank, len(graph[u]) + len(graph[v]) - (u in graph[v]))
        return rank