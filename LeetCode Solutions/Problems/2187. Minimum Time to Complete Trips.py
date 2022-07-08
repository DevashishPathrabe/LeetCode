class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low, high = 1, totalTrips * min(time)
        def helper(x):
            return sum(x // t for t in time) >= totalTrips
        while low < high:
            mid = (low + high) // 2
            if not helper(mid):
                low = mid + 1
            else:
                high = mid
        return low