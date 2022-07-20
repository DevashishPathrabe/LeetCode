class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            arr = []
            for index, i in enumerate(range(0, len(nums), 2)):
                if index % 2 == 0:
                    arr.append(min(nums[i], nums[i + 1]))
                else:
                    arr.append(max(nums[i], nums[i + 1]))
            nums = arr
        return nums[0]