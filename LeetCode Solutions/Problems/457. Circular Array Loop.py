class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            st = i
            k = i
            f = nums[i] > 0
            j = 0
            while j < len(nums):
                step = nums[k]
                if f and step < 0:
                    break
                if not f and step > 0:
                    break
                k += step
                k %= len(nums)
                j += 1
                if k == st and j > 1:
                    return True
                elif k == st and j <= 1:
                    break
        return False