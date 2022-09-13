class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        fresh_avail = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh_avail += 1
        minutes = 0
        while q and fresh_avail > 0:
            minutes += 1
            rottens = []
            current_rotten = len(q)
            for _ in range(current_rotten):
                rotten = q.popleft()
                cases = [(0, 1), (0,-1), (1, 0), (-1,0)]
                for case in cases:
                    new_rotten = rotten[0] + case[0], rotten[1] + case[1]
                    if (0 <= new_rotten[0] < m) and (0 <= new_rotten[1] < n) and grid[new_rotten[0]][new_rotten[1]] == 1:
                        q.append(new_rotten)
                        grid[new_rotten[0]][new_rotten[1]] = 2
                        fresh_avail -= 1
        if fresh_avail > 0:
            return -1
        return minutes