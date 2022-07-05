class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int time = 0;
        for (int i=0; i<points.length-1; i++){
            int x = points[i][0] - points[i+1][0];
            int y = points[i][1] - points[i+1][1];
            time += Math.max(Math.abs(x), Math.abs(y));
        }
        return time;
    }
}