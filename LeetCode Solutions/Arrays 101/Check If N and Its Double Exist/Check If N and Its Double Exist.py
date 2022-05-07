class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashSet = set()
        for i in range(len(arr)):
            if ((arr[i]*2 in hashSet) or (arr[i]%2 == 0 and arr[i]//2 in hashSet)):
                return True
            hashSet.add(arr[i])
        return False