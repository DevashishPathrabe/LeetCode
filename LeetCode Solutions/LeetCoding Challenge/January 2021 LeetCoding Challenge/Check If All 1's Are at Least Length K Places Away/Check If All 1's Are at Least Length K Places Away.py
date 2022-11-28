class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0;
        for i in range(len(nums)):
            if (nums[i] == 1 and count < k and i != 0):
                return False
            elif (nums[i] == 1):
                count = 0
            else:
                count += 1
        return True