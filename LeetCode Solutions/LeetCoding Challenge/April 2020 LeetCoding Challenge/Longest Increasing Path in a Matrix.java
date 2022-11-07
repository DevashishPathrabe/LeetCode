class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        int ylen = matrix.length, xlen = matrix[0].length, result = 0;
        int[][] memo = new int[ylen][xlen];
        for (int i=0; i<ylen; i++)
            for (int j=0; j<xlen; j++)
                result = Math.max(result, helper(i, j, matrix, memo));
        return result;
    }
    public int helper(int y, int x, int[][] matrix, int[][] memo) {
        if(memo[y][x] > 0){
            return memo[y][x];
        }
        int value = matrix[y][x];
        memo[y][x] = 1 + Math.max(
            Math.max(y < matrix.length - 1 && matrix[y+1][x] < value ? helper(y+1, x, matrix, memo) : 0,
                    y > 0 && matrix[y-1][x] < value ? helper(y-1, x, matrix, memo) : 0),
            Math.max(x < matrix[0].length - 1 && matrix[y][x+1] < value ? helper(y, x+1, matrix, memo) : 0,
                    x > 0 && matrix[y][x-1] < value ? helper(y, x-1, matrix, memo) : 0));
        return memo[y][x];
    }
}