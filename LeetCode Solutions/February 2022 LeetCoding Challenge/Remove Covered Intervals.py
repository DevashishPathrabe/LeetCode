class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda a:(a[0], -a[1]))
        j = 0
        result = len(intervals)
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                result -= 1
            else:
                j = i
        return result