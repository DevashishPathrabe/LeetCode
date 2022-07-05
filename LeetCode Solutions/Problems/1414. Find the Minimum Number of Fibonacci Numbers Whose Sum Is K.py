class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        if k == 1:
            return 1
        fib = [1, 1]
        temp = fib[-2]
        while fib[-1] <= k:
            fib.append(fib[-1] + temp)
            temp = fib[-2]
        fib.pop()
        current = k
        result = 0
        for each in range(len(fib)-1, -1, -1):
            if current == 0:
                return result
            if fib[each] <= current:
                result += 1
                current -= fib[each]
        return result