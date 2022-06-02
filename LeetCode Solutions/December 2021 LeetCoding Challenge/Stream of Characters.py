class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ''
        self.dict = collections.defaultdict(set)
        for i in words:
            self.dict[i[-1]].add(i)

    def query(self, letter: str) -> bool:
        self.s += letter
        return any(self.s.endswith(i) for i in self.dict[letter])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)