class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def backtrack(grid,i,j,row,column):
            if(i>=row or j>=column or i<0 or j<0):
                return
            if(grid[i][j]=="2" or grid[i][j]=="0"):
                return
            grid[i][j]="2"
            backtrack(grid,i+1,j,row,column)
            backtrack(grid,i-1,j,row,column)
            backtrack(grid,i,j+1,row,column)
            backtrack(grid,i,j-1,row,column)
            return
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=="1"):
                    backtrack(grid,i,j,len(grid),len(grid[0]))
                    total+=1
        return total