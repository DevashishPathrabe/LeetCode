class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        A = list(map(str, nums))
        if len(A) <= 2:
            return '/'.join(A)
        return A[0] + '/(' + '/'.join(A[1:]) + ')'