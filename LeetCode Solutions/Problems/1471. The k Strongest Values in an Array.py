class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        result, i, j = [], 0, len(arr) - 1
        while i <= j and k:
            if abs(arr[i] - median) > abs(arr[j] - median):
                result.append(arr[i])
                i += 1
            else:
                result.append(arr[j])
                j -= 1       
            k -= 1
        return result