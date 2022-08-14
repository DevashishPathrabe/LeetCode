class Solution:

    def __init__(self, w: List[int]):
        self.accWeight = list(accumulate(w))

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.accWeight, random.randint(1, self.accWeight[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()