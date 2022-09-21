class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []
        self.m = []
    def push(self, x: int) -> None:
        self.a.append(x)
        m = self.m
        m.append(x if not m else min(x, m[-1]))
    def pop(self) -> None:
        self.a.pop()
        self.m.pop()
    def top(self) -> int:
        return self.a[-1]
    def getMin(self) -> int:
        return self.m[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()