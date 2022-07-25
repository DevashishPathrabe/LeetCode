class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, i):
            if(i == len(nums)):
                output.append(nums[:])
                return
            appeared = set()
            for j in range(i, len(nums)):
                if(nums[j] in appeared):
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                helper(nums, i + 1)
                nums[i], nums[j] = nums[j], nums[i]
                appeared.add(nums[j])
        output = []
        helper(nums, 0)
        return output