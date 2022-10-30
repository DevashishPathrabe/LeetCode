class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k > m + n - 3:
            return m + n - 2
        q = deque([(0, k, 0, 0)])
        visited = set([(k, 0, 0)])
        while q:
            count, obstacles, x, y = q.popleft()
            if x == m-1 and y == n-1:
                return count
            for newX, newY in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                if not (0 <= newX < m and 0 <= newY < n):
                    continue
                cell = grid[newX][newY]
                if obstacles - cell >= 0 and (obstacles - cell, newX, newY) not in visited:
                    q.append((count + 1,  obstacles - cell, newX, newY))
                    visited.add((obstacles - cell, newX, newY))
        return -1