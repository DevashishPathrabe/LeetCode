class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return list(self.nums)

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = list(self.nums)
        B = []
        while nums:
            i = random.randint( 0 , len(nums) - 1 )
            nums[i], nums[-1] = nums[-1], nums[i]
            B.append( nums.pop() )
        return B

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()