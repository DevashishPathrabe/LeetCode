class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0:-1}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            remainder = total % k 
            if remainder in seen:
                if i - seen[remainder] > 1:
                    return True
            else:
                seen[remainder] = i
        return False