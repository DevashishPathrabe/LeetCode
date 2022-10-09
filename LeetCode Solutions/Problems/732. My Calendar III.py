from sortedcontainers import SortedDict
class MyCalendarThree:

    def __init__(self):
        self.calendar = SortedDict()

    def book(self, start: int, end: int) -> int:
        if start in self.calendar:
            self.calendar[start] += 1
        else:
            self.calendar[start] = 1
        if end in self.calendar:
            self.calendar[end] += -1
        else:
            self.calendar[end] = -1
        counter, maxNo = 0, 0
        for key in self.calendar.keys():
            counter += self.calendar[key]
            maxNo = max(maxNo,counter)
        return maxNo


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)