class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i, j = 0, len(arr)-1
        while(j-i+1 != k):
            leftDifference = abs(arr[i] - x)
            rightDifference = abs(arr[j] - x)
            if(leftDifference > rightDifference):
                i += 1
            else:
                j -= 1
        return arr[i:j+1]