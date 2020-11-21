class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = {}

    def insert(self, key: str, val: int) -> None:
        self.values[key] = val

    def sum(self, prefix: str) -> int:
        totalSum = 0
        for key in self.values.keys():
            try:
                if(key[:len(prefix)] == prefix):
                    totalSum += self.values[key]
            except:
                continue
        return totalSum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)