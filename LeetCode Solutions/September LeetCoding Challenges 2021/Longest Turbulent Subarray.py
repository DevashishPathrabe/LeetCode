class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        increment, decrement, result = 1, 1, 1
        for i in range(1, len(arr)):
            if (arr[i] < arr[i-1]):
                decrement = increment + 1
                increment = 1
            elif (arr[i] > arr[i-1]):
                increment = decrement + 1
                decrement = 1
            else:
                increment = 1
                decrement = 1
            result = max(result, max(increment, decrement))
        return result