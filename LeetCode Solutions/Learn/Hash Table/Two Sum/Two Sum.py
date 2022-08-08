class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            try:
                temp = target - nums[i]
                hashmap[temp] += 0
                return [hashmap[temp], i]
            except:
                hashmap[nums[i]] = i