class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [nums[0]]
            else:
                return nums
        count = {}
        freq = (len(nums) // 3) + 1 
        result = []
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                temp = count[num] + 1
                count[num] = temp
                if temp == freq:
                    result.append(num)
        return result