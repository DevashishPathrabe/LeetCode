class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        position = []
        if (target not in nums):
            return[-1, -1]
        count = 0
        for i in range(len(nums)):
            if (nums[i] == target):
                position.append(i)
                i += 1
                count += 1
        if (count < 2):
            position.append(position[-1])
        return position[0], position[-1]