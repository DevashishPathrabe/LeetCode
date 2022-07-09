class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        p = None
        count = 0
        for i, n in enumerate(self.nums):
            if n == target:
                count += 1
                prob = 1 / (count)
                if random.random() < prob:
                    p = i
        return p


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)