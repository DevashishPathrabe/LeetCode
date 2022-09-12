class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = collections.defaultdict(list)
        for a, b in connections:
            edges[a].append((b, 1))
            edges[b].append((a, 0))
        def helper(i, p):
            return sum(d + helper(j, i) for j, d in edges[i] if j != p)
        return helper(0, -1)