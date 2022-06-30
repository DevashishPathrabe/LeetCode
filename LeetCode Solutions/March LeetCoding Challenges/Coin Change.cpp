class Solution {
    int fewestNumberOfCoins = 10001;
public:
    int coinChange(vector<int>& coins, int amount) {
        sort(coins.begin(), coins.end());
        recursiveFunction(amount, 0, coins.size()-1, coins);
        return fewestNumberOfCoins < 10001 ? fewestNumberOfCoins : -1;
    }
    void recursiveFunction(int amount, int num, int coinIndex, vector<int>& coins) {
        if(!amount){
            fewestNumberOfCoins = min(num, fewestNumberOfCoins);
        }
        else if(amount > 0 && ~coinIndex){
            int n = amount / coins[coinIndex];
            if(n + num >= fewestNumberOfCoins){
                return;
            }
            while(~n){
                recursiveFunction(amount - n * coins[coinIndex], num + n--, coinIndex - 1, coins);
            }
        }
    }
};