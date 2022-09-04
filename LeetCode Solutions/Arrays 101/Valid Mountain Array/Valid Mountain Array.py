class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if (len(A) < 3):
            return False
        i = 1
        while ((i < len(A)) and (A[i-1] < A[i])):
            i += 1
        if ((i == len(A)) or (i == 1)):
            return False
        while ((i < len(A)) and (A[i-1] > A[i])):
            i += 1
        return len(A) == i