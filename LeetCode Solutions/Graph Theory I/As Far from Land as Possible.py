class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque([])
        m = len(grid)
        n = len(grid[0])
        level = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append([i,j])
        if len(q) == 0 or len(q) == (m*n):
            return -1
        while(q):
            size = len(q)
            while(size):
                node = q.popleft()
                i,j = node[0],node[1]
                if i-1 >= 0 and grid[i-1][j] == 0:
                    grid[i-1][j] = 1
                    q.append([i-1,j])
                if j-1 >= 0 and grid[i][j-1] == 0:
                    grid[i][j-1] = 1
                    q.append([i, j-1])
                if i+1 <= m-1 and grid[i+1][j] == 0:
                    grid[i+1][j] = 1
                    q.append([i+1, j])
                if j+1 <= n-1 and grid[i][j+1] == 0:
                    grid[i][j+1] = 1
                    q.append([i, j+1])
                size -= 1
            level += 1
        return level-1