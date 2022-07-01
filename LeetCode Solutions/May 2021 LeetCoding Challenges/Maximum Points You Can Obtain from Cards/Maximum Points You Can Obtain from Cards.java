class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int total = 0;
        for(int i=0; i<k; i++){
            total += cardPoints[i];
        }
        int maximumScore = total;
        for(int i=k-1, j=cardPoints.length-1; i>=0; i--, j--){
            total += cardPoints[j] - cardPoints[i];
            maximumScore = Math.max(maximumScore, total);
        }
        return maximumScore;
    }
}