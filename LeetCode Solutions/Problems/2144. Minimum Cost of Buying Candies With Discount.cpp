class Solution {
public:
    int minimumCost(vector<int>& cost) {
        sort(cost.begin(), cost.end());
        int minCost = 0, n = cost.size();
        for (int i=0; i<cost.size(); ++i){
            if (i % 3 != n % 3){
                minCost += cost[i];
            }
        }
        return minCost;
    }
};