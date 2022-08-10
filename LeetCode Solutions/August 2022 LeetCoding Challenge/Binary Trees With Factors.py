class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        fmap, binaryTrees = defaultdict(), 0
        for num in arr:
            ways, lim = 1, sqrt(num)
            for fA in arr:
                if(fA > lim):
                    break
                fB = num / fA
                if(fB in fmap):
                    ways += fmap[fA] * fmap[fB] * (1 if fA == fB else 2)
            fmap[num], binaryTrees = ways, (binaryTrees + ways)
        return binaryTrees % 1000000007