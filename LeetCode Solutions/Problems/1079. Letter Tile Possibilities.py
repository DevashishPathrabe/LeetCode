class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        List = list(tiles)
        Sum =0
        for i in range(1, len(List)+1):
            k = len(list(set(list(permutations(List, i)))))
            Sum += k
        return Sum