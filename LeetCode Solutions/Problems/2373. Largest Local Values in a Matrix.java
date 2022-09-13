class Solution {
    public int[][] largestLocal(int[][] grid) {
        int n = grid.length;
        int[][] result = new int[n - 2][n - 2];
        for (int i=0;i<n-2;i++){
            for (int j=0;j<n-2;j++){
                result[i][j] = maxMatrix(grid, i, j);
            }
        }
        return result;
    }
    
    public int maxMatrix(int[][] grid, int row, int column) {
        int maxValue = Integer.MIN_VALUE;
        for (int i=row;i<(row+3);i++){
            for (int j=column;j<(column+3);j++){
                if (grid[i][j] > maxValue){
                    maxValue = grid[i][j];
                }
            }
        }
        return maxValue;
    }
}