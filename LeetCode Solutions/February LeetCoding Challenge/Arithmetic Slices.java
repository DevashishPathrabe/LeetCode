class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        int arithmeticSlices = 0, combination = 0, lastDifference = 0;
        for(int i=0; i<A.length-1; i++){
            int difference = A[i+1] - A[i];
            if(i!=0 && difference == lastDifference){
                combination += 1;
                arithmeticSlices += combination;
            } else{
                combination = 0;
            }
            lastDifference = difference;
        }
        return arithmeticSlices;
    }
}