class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = []

    def add(self, key: int) -> None:
        self.value.append(key)

    def remove(self, key: int) -> None:
        self.value = [i for i in self.value if(i!=key)]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.value


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)