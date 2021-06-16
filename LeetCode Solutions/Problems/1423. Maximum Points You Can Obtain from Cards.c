

int maxScore(int* cardPoints, int cardPointsSize, int k){
    int total = 0;
    for(int i=0; i<k; i++){
        total += cardPoints[i];
    }
    int maximumScore = total;
    for(int i=k-1, j=cardPointsSize-1; i>=0; i--, j--){
        total += cardPoints[j] - cardPoints[i];
        maximumScore = fmax(maximumScore, total);
    }
    return maximumScore;
}