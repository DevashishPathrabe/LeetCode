class Solution:

    def __init__(self, m: int, n: int):
        self.rows = m
        self.cols = n
        self.len_range = m * n
        self.upper_limit = self.len_range - 1
        self.used = set()

    def flip(self) -> List[int]:
        val = randint(0, self.upper_limit)
        while val in self.used:
            val += 1
            if val == self.len_range:
                val = 0
        self.used.add(val)
        return list(divmod(val, self.cols))

    def reset(self) -> None:
        self.used = set()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()