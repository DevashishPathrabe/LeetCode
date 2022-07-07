class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        sort(coins.begin(), coins.end());
        int n = coins.size();
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
};