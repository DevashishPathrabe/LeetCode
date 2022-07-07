class Solution:
    def twoEggDrop(self, n: int) -> int:
        minimumNumberOfMoves = 0
        iterable = n
        while iterable > 0:
            minimumNumberOfMoves += 1
            iterable -= minimumNumberOfMoves
        return minimumNumberOfMoves