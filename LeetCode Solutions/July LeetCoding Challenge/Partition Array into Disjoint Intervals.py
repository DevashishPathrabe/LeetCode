class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        max = nums[0]
        for i in range(len(nums)-1):
            flag = 1
            if nums[i] > max:
                max = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] < max:
                    flag = 0
                    break
            if flag == 1:
                return i+1
        return 0;