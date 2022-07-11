from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.calendar = SortedDict()

    def book(self, start: int, end: int) -> bool:
        if start in self.calendar:
            self.calendar[start] += 1
        else:
            self.calendar[start] = 1
        if end in self.calendar:
            self.calendar[end] += -1
        else:
            self.calendar[end] = -1
        counter = 0
        for key in self.calendar.keys():
            counter += self.calendar[key]
            if counter > 2:
                self.calendar[start] += -1
                self.calendar[end] += 1
                if self.calendar[start] == 0:
                    del self.calendar[start]
                if self.calendar[end] == 0:
                    del self.calendar[end]
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)