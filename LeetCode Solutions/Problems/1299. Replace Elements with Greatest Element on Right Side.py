class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestElement = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], greatestElement = greatestElement, max(arr[i], greatestElement)
        return arr