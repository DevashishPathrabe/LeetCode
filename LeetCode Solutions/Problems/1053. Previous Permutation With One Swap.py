class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)-1
        left = n
        while left >= 0 and arr[left] >= arr[left-1]:
            left -= 1
        if left <= 0:
            return arr
        k = left - 1
        right = n
        while right >= left:
            if arr[right] < arr[k] and arr[right] != arr[right-1]:
                arr[k], arr[right] = arr[right], arr[k]
                return arr
            right -= 1
        return arr