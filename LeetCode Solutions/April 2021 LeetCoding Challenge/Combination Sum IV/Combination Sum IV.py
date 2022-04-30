class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        arr = [0] * (target+1)
        arr[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if (num <= i):
                    arr[i] += arr[i-num]
        return arr[target]