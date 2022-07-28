class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        for(int i=0; i<grid.length; i++){
           for(int j=0; j<grid[0].length; j++){
               if(grid[i][j]==1){
                   int islandArea = helper(grid, i, j);
                   if(islandArea>maxArea){
                       maxArea = islandArea;
                   }
               }
           }
        }
        return maxArea;
    }
    public int helper(int[][] grid, int i, int j){
        if(i>=0 && i<grid.length && j>=0 && j<grid[0].length && grid[i][j] == 1){
            grid[i][j] = 0;
            return(helper(grid, i+1, j) + helper(grid, i-1, j) + helper(grid, i, j-1) + helper(grid, i, j+1)) + 1;
        }
        return 0;
    }
}