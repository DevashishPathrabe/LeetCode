class MyCalendar:

    def __init__(self):
        self.calendar = {'start': -1, 'end': -1, 'next': {'start': float('inf'), 'end': float('inf')}}

    def book(self, start: int, end: int) -> bool:
        current = self.calendar
        while(current['start'] < start):
            last, current = current, current['next']
        if(last['end'] > start or current['start'] < end):
            return False
        last['next'] = {'start': start, 'end': end, 'next': current}
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)