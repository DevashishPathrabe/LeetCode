class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        heap = []
        for index, num in enumerate(nums):
            num, temp = str(num), 0
            for i in range(len(num)):
                temp += mapping[int(num[i])] * 10 ** (len(num) - i - 1)
            heapq.heappush(heap, (temp, index))
        ans = []
        while heap:
            ans.append(nums[heapq.heappop(heap)[1]])
        return ans