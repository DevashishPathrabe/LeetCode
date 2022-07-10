class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        source, target = 1000000000, 0
        stack = []
        nums = list(str(num))
        for i, c in enumerate(nums):
            j = i
            while stack and stack[-1] < c:
                stack.pop()
                if len(stack) <= source:
                    source, target = len(stack), i
            if target and c == nums[target] and i > target:
                target = i
            stack.append(c)
        if target:
            nums[source], nums[target] = nums[target], nums[source]
            return int("".join(nums))
        return num