class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left, right = 0, len(A)-1
        while (left < right):
            if (A[left] % 2 == 1):
                A[left], A[right] = A[right], A[left]
                right -= 1
            else:
                left += 1
        return A