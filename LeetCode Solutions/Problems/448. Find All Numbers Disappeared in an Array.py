class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num1 = set(nums)
        num2 = set(range(1, len(nums)+1))
        return num2-num1