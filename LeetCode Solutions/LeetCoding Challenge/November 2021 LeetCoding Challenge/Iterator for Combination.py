class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combination = list(combinations(characters, combinationLength))
        self.stack = 0

    def next(self) -> str:
        temp = ''.join(self.combination[self.stack])
        self.stack +=1
        return temp

    def hasNext(self) -> bool:
        return self.stack <= len(self.combination) - 1


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()