

int minTimeToVisitAllPoints(int** points, int pointsSize, int* pointsColSize){
    int time = 0;
    for (int i=0; i<pointsSize-1; i++){
        int x = points[i][0] - points[i+1][0];
        int y = points[i][1] - points[i+1][1];
        time += fmax(abs(x), abs(y));
    }
    return time;
}