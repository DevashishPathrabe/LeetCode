class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted((a, b, c))
        difference1 = b-a-1
        difference2 = c-b-1
        if difference1 == 0 and difference2 == 0:
            minimum = 0
        elif difference1 == 0 or difference2 == 0 or difference1 == 1 or difference2 == 1:
            minimum = 1
        else:
            minimum = 2
        return [minimum, difference1 + difference2]