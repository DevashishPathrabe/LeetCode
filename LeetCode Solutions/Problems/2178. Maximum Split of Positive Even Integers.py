class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1:
            return []
        x = int(((4 * finalSum + 1) ** 0.5 - 1) / 2)
        leftover = finalSum - x * (x + 1)
        return list(range(2, 2 * x, 2)) + [2 * x + leftover]