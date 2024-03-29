class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0
        while len(arr) > 1:
            minIndex = arr.index(min(arr))
            if 0 < minIndex < len(arr) - 1:
                ans += min(arr[minIndex - 1], arr[minIndex + 1]) * arr[minIndex]
            else:   
                ans += arr[1 if minIndex == 0 else minIndex - 1] * arr[minIndex]
            arr.pop(minIndex)
        return ans