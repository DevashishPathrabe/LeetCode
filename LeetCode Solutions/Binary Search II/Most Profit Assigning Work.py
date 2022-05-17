class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        indexes = sorted(range(n), key=lambda x:difficulty[x])
        difficulty.sort()
        max_profit = []
        mx = 0
        for i in range(n):
            mx = max(mx, profit[indexes[i]])
            max_profit.append(mx)
        result = 0
        for w in worker:
            idx = bisect.bisect(difficulty, w) - 1
            if idx < 0:
                continue
            result += max_profit[idx]
        return result