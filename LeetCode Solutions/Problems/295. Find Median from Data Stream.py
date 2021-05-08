class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []
        self.h = len(self.a) // 2

    def addNum(self, num: int) -> None:
        self.a.append(num)
        self.a.sort()
        self.h = len(self.a) // 2

    def findMedian(self) -> float:
        if(len(self.a) == 0):
            return 0
        if(len(self.a) % 2 == 0):
            return (self.a[self.h] + self.a[self.h-1]) / 2
        return self.a[self.h]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()