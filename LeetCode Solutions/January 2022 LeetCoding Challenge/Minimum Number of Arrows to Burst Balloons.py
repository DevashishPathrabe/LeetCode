class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points:
            points.sort(key = lambda x: x[0])
            result = [points[0]]
            for i in range(1, len(points)):
                start,end = points[i]
                if result[-1][1] >= start:
                    result[-1][0] = min(start, result[-1][0])
                    result[-1][1] = min(end, result[-1][1])
                else:
                    result.append([start,end])
            return len(result)
        else:
            return 0