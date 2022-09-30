class Solution {
    int fewestNumberOfCoins = 10001;
    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        recursiveFunction(amount, 0, coins.length-1, coins);
        return fewestNumberOfCoins < 10001 ? fewestNumberOfCoins : -1;
    }
    void recursiveFunction(int amount, int num, int coinIndex, int[] coins) {
        if (amount == 0){
            fewestNumberOfCoins = Math.min(num, fewestNumberOfCoins);
        }
        else if (amount > 0 && coinIndex >= 0){
            int n = amount / coins[coinIndex];
            if (n + num >= fewestNumberOfCoins){
                return;
            }
            while (n >= 0){
                recursiveFunction(amount - n * coins[coinIndex], num + n--, coinIndex - 1, coins);
            }
        }
    }
}