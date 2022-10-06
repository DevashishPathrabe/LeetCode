class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.hmap[key]
        l = 0
        h = len(values) - 1
        while l <= h:
            mid = (l+h) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] > timestamp:
                h = mid-1
            else:
                l = mid+1  
        return "" if h < 0 else values[h][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)