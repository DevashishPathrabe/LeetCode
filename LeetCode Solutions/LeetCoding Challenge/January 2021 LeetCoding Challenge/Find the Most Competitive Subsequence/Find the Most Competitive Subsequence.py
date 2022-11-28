class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        if (len(nums) == k):
            return nums
        stack = []
        length = len(nums)
        for (i, num) in enumerate(nums):
            if (length - i + len(stack) <= k):
                stack.append(num)
            else:
                while (length - i + len(stack) > k and len(stack) > 0 and stack[-1] > num):
                    stack.pop()
                if (len(stack) < k):
                    stack.append(num)
        return stack