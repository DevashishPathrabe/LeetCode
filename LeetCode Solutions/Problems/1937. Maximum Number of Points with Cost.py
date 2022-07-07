class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        for i in range(1, n):
            runningMax = 0
            leftChange = [0]*m
            for j in range(m):
                runningMax = max(runningMax-1, points[i-1][j])
                leftChange[j] = runningMax
            runningMax = 0
            rightChange = [0]*m
            for j in range(m-1,-1,-1):
                runningMax = max(runningMax-1, points[i-1][j]) 
                rightChange[j] = runningMax
            for j in range(m):
                points[i][j] += max(leftChange[j], rightChange[j])
        return max(points[-1])