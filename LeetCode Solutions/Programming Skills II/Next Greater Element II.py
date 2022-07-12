class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = nums[::-1]
        result = []
        for value in reversed(nums):
            while stack and value >= stack[-1]:
                stack.pop()
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)
            stack.append(value)
        return result[::-1]