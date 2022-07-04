class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        L, C = len(barcodes), collections.Counter(barcodes)
        barcodes.sort(key = lambda x: (C[x],x))
        barcodes[1::2], barcodes[::2] = barcodes[:L//2], barcodes[L//2:]
        return barcodes