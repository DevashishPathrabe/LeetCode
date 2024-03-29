class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        difference = abs(arr[0] - arr[1])
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) != difference:
                return False
        return True