class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if(len(arr) < 3):
            return False
        for i in range(len(arr)-1):
            if(arr[i+1] <= arr[i]):
                break;
        for j in range(len(arr)-1, 0, -1):
            if(arr[j-1] <= arr[j]):
                break
        return i == j