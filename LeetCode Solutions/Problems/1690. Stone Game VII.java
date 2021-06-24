class Solution {
    public int stoneGameVII(int[] stones) {
        int[] dpCurrent = new int[stones.length], dpLast = new int[stones.length];
        for(int i=stones.length-2; i>=0; i--){
            int total = stones[i];
            int[] temp = dpLast;
            dpLast = dpCurrent;
            dpCurrent = temp;
            for(int j=i+1; j<stones.length; j++){
                total += stones[j];
                dpCurrent[j] = Math.max(total-stones[i] - dpLast[j], total - stones[j] - dpCurrent[j-1]);
            }
        }
        return dpCurrent[stones.length-1];
    }
}