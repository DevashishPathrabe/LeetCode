class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, val: int) -> None:
        heapq.heappush(self.intervals, [val, val])

    def getIntervals(self) -> List[List[int]]:
        temp = []
        while self.intervals:
            current = heapq.heappop(self.intervals)
            if temp and current[0] <= temp[-1][1] + 1:
                temp[-1][1] = max(temp[-1][1], current[1])
            else:
                temp.append(current)
        self.intervals = temp
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()