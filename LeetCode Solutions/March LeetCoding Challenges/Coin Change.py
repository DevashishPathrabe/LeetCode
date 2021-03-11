class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        fewestNumberOfCoins = 10001
        def recursiveFunction(amount, num, coinIndex):
            nonlocal fewestNumberOfCoins
            if(amount == 0):
                if(num < fewestNumberOfCoins):
                    fewestNumberOfCoins = num
            elif(amount > 0 and ~coinIndex):
                n = ceil(amount / coins[coinIndex])
                if(num + n >= fewestNumberOfCoins):
                    return
                for i in range(n, -1, -1):
                    recursiveFunction(amount - i * coins[coinIndex], num + i, coinIndex - 1)
        recursiveFunction(amount, 0, len(coins)-1)
        if(fewestNumberOfCoins < 10001):
            return fewestNumberOfCoins
        else:
            return -1