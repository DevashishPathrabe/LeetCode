class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, midElement = [], float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < midElement:
                return True
            while stack and nums[i] > stack[-1]:
                midElement = stack.pop()
            stack.append(nums[i])
        return False