class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        positive = [0] * n
        negative = [0] * n
        if nums[0] > 0:
            positive[0] = 1
        else:
            positive[0] = 0
        if nums[0] < 0:
            negative[0] = 1
        else:
            negative[0] = 0
        for i in range(1, n):
            if nums[i] < 0:
                if negative[i - 1]:
                    positive[i] = 1 + negative[i - 1]
                else:
                    positive[i] = 0
                if positive[i - 1]:
                    negative[i] = 1 + positive[i - 1]
                else:
                    negative[i] = 1
            elif nums[i] > 0:
                if positive[i - 1]:
                    positive[i] = 1 + positive[i - 1]
                else:
                    positive[i] = 1
                if negative[i - 1]:
                    negative[i] = 1 + negative[i - 1]
                else:
                    negative[i] = 0
        return max(positive)