class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        lastFinish = 0
        WaitingTime = 0
        n = len(customers)
        for i, j in customers:
            currentStart = max(i, lastFinish)
            WaitingTime += currentStart + j - i
            lastFinish = currentStart + j
        return WaitingTime / n