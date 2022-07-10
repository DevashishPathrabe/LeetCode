class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if(not timeSeries):
            return 0
        previous = timeSeries[0] 
        poison = duration
        for i in range(1, len(timeSeries)):
            if(previous + duration >= timeSeries[i]):
                overlap = previous + duration - timeSeries[i]
                poison += duration - overlap
            else:
                poison += duration
            previous = timeSeries[i]
        return poison