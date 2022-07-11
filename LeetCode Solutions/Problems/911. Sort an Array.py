class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda a: a)
        return nums