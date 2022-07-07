class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            arr = nums[:i] + nums[i+1:]
            count = 0
            for j in range(1, len(arr)):
                if arr[j] <= arr[j-1]:
                    break
                else:
                    count += 1
            if count == len(arr)-1:
                return True
        return False