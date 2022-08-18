class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l = 1
        h = max(dist)*(100)
        def fun(speed):
            time = 0
            for i in dist[:-1]:
                time += ceil(i/speed)
            time += dist[-1]/speed
            if time <= hour:
                return True
            return False
        ans=98765432
        while(l <= h):
            mid = l+(h-l)//2
            if fun(mid):
                ans = min(mid,ans)
                h = mid-1
            else:
                l = mid+1
        if ans == 98765432:
            return -1
        return ans