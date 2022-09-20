class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        if (len(intervals) < 2):
            return intervals        
        start = intervals[0][0]
        end = intervals[0][1]
        output = []
        for i in range(1, len(intervals)):
            if (intervals[i][0] <= end):
                end = max(intervals[i][1], end)
            else:
                output.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        output.append([start, end])
        return output