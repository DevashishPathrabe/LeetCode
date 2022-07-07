class Solution {
    public int getMaximumConsecutive(int[] coins) {
        Arrays.sort(coins);
        int n = coins.length;
        int current = 1;
        for (int i=0; i<n; i++){
            if (coins[i] <= current){
               current += coins[i];
            } else{
                break;
            }
        }
        return current;
    }
}