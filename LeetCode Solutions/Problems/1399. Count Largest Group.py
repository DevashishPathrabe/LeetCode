class Solution:
    def countLargestGroup(self, n: int) -> int:
        def findSum(n):
            currentSum = 0
            while (n > 0):
                currentSum += n % 10
                n = n//10
            return currentSum
        di = Counter()
        for i in range(1, n+1):
            sumOfDigit = findSum(i)            
            di[sumOfDigit] += 1
        value = list(di.values())
        maxLength = max(value)
        group = value.count(maxLength)
        return group