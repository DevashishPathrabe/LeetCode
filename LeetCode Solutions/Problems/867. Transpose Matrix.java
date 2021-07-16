class Solution {
    public int[][] transpose(int[][] matrix) {
        int height = matrix.length;
        int width = matrix[0].length;
        int[][] transpose = new int[width][height];
        for (int i=0; i<height; i++) {
            for (int j=0; j<width; j++) {
                transpose[j][i] = matrix[i][j];
            }
        }
        return transpose;
    }
}