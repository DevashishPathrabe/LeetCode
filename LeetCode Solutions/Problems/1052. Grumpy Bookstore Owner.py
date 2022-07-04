class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        result = 0
        for i in range(n):
            if grumpy[i] == 0:
                result += customers[i]
        Sum = 0        
        for i in range(minutes):
            if grumpy[i] == 1:
                Sum += customers[i]
        sol = Sum
        for r in range(minutes, n):
            if grumpy[r] == 1:
                Sum += customers[r]
            if grumpy[r - minutes] == 1:
                Sum -= customers[r - minutes]
            sol = max(Sum, sol)
        return result + sol