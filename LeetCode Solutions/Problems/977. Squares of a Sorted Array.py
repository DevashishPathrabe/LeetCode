class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(number * number for number in A)