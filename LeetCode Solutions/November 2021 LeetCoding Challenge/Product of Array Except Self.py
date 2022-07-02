class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArray = [1] * len(nums)
        for i in range(1, len(nums)):
            outputArray[i] = nums[i-1] * outputArray[i-1]
        rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            outputArray[i] *= rightProduct
            rightProduct *= nums[i]
        return outputArray