class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while(left < right):
            middle = left + (right-left) // 2
            start, count = 0, 0
            for i in range(n):
                while(nums[i] - nums[start] > middle):
                    start += 1
                count += i - start
            if(count < k):
                left = middle + 1
            else:
                right = middle
        return left