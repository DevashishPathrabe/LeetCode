class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxSlidingWindow, d = [], deque()
        for i in range(len(nums)):
            if(d and d[0] < i-k):
                d.popleft()
            while(d and nums[d[-1]] < nums[i]):
                d.pop()
            d.append(i)
            if(i > k-2):
                maxSlidingWindow.append(nums[d[0]])
        return maxSlidingWindow