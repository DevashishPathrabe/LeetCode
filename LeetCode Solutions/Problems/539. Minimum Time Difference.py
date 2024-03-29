class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def helper(time_str):
            h, m = time_str.split(':')
            return int(h) * 60 + int(m)
        total, minutes = 24 * 60, sorted([helper(time_str) for time_str in timePoints])
        n, difference = len(minutes), total - (minutes[-1] - minutes[0])
        for i in range(1, n):
            if (current := minutes[i] - minutes[i - 1]) < difference:
                difference = current
        return difference