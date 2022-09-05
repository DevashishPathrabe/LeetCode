class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid),len(grid[0])
        ans = []
        def dfs(arr, i, j, n, m):
            while i < n and j < m and i > -1 and j > -1:
                if arr[i][j] == 1:
                    if j + 1 < m and arr[i][j + 1] == 1:
                        i += 1
                        j += 1
                    else:
                        return -1
                else:
                    if j - 1 > -1 and arr[i][j - 1] == -1:
                        i += 1
                        j -= 1
                    else:
                        return -1
            return j
        for j in range(m):
            ans.append(dfs(grid, 0, j, n, m))
        return ans