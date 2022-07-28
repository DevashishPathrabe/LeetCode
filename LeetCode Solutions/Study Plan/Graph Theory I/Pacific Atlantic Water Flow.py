if(not heights):
            return heights
        x, y = len(heights[0]), len(heights)
        listOfGridCoordinates, dp = [], [0] * (x * y)
        def dfs(i: int, j: int, w: int, h: int):
            ij = i * x + j
            if(dp[ij] & w or heights[i][j] < h):
                return
            dp[ij] += w
            h = heights[i][j]
            if(dp[ij] == 3):
                listOfGridCoordinates.append([i,j])
            if(i + 1 < y):
                dfs(i+1, j, w, h)
            if(i > 0):
                dfs(i-1, j, w, h)
            if(j + 1 < x):
                dfs(i, j+1, w, h)
            if(j > 0):
                dfs(i, j-1, w, h)
        for i in range(y):
            dfs(i, 0, 1, heights[i][0])
            dfs(i, x-1, 2, heights[i][x-1])
        for j in range(x):
            dfs(0, j, 1, heights[0][j])
            dfs(y-1, j, 2, heights[y-1][j])
        return listOfGridCoordinates