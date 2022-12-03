class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int buying = 0, selling = -prices[0];
        for (int i=1; i<prices.size(); i++){
            buying = max(buying, selling + prices[i] - fee);
            selling = max(selling, buying - prices[i]);
        }
        return buying;
    }
};