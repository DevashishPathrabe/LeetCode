class Solution {
    public int minimumCost(int[] cost) {
        Arrays.sort(cost);
        int minCost = 0, n = cost.length;
        for (int i=0; i<n; ++i){
            if (i % 3 != n % 3){
                minCost += cost[i];
            }
        }
        return minCost;
    }
}