class RandomizedCollection:

    def __init__(self):
        self.multiSet = []

    def insert(self, val: int) -> bool:
        inMultiSet = val in self.multiSet
        self.multiSet.append(val)
        return not inMultiSet

    def remove(self, val: int) -> bool:
        inMultiSet = val in self.multiSet
        if inMultiSet:
            self.multiSet.remove(val)
        return inMultiSet

    def getRandom(self) -> int:
        return self.multiSet[random.randint(0, len(self.multiSet)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()