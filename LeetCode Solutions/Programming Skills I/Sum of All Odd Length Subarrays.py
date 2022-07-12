class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subarraysSum = 0
        for i in range(len(arr) + 1):
            for j in range(i):
                x = arr[j:i]
                if x and len(x) % 2 != 0:
                    subarraysSum += sum(x)
        return subarraysSum