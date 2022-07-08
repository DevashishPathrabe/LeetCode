class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = Counter()
        for i in range(len(nums)):
            if nums[i] == key and i < len(nums) -1:
                count[nums[i+1]] += 1
        return count.most_common()[0][0]