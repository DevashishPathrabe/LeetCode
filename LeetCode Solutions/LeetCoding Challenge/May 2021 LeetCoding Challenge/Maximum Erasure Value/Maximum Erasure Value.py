class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        nmap, Sum, maximumScore, left = [0] * 10001, 0, 0, 0
        for right in nums:
            nmap[right] += 1
            Sum += right
            while nmap[right] > 1:
                nmap[nums[left]] -= 1
                Sum -= nums[left]
                left += 1
            maximumScore = max(maximumScore, Sum)
        return maximumScore