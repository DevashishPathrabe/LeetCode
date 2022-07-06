class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current = (0, 0)
        direction, visited = dict(N=(0, 1), S=(0, -1), E=(1, 0), W=(-1, 0)), set([current])
        for p in path:
            current = tuple(sum(t) for t in zip(current, direction[p]))
            if current in visited:
                return True
            visited.add(current)
        return False