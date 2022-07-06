class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = minimum = productSubarray = nums[0]
        for i in range(1, len(nums)):
            maximum, minimum = max(maximum*nums[i], minimum*nums[i], nums[i]), min(maximum*nums[i], minimum*nums[i], nums[i])
            productSubarray = max(productSubarray, maximum)
        return productSubarray