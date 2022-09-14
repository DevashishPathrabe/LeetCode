class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        closest = -1
        closedDist = float('inf')
        for i in range(len(points)):
            if x == points[i][0] or y == points[i][1]:
                dist = abs(x-points[i][0]) + abs(y-points[i][1])
                if dist < closedDist:
                    closedDist = dist
                    closest = i
        return closest