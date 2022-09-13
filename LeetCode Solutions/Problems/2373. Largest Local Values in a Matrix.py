class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        column = len(grid[0])
        finalMatrix = []
        for i in range(row-2):
            answer = []
            for j in range(column-2):
                arr = []
                arr += grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]
                answer.append(max(arr))
            finalMatrix.append(answer)
        return finalMatrix