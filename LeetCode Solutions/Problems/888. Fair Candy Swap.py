class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        difference = (sum(aliceSizes) - sum(bobSizes)) // 2
        aliceSizes = set(aliceSizes)
        for candy in set(bobSizes):
            if difference + candy in aliceSizes:
                return [difference + candy, candy]