class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def helper(needs):
            if needs == [0] * m:
                return 0
            if tuple(needs) in d:
                return d[tuple(needs)]
            result = 0
            for i in range(m):
                result += needs[i] * price[i]
            for sp in special:
                for i in range(len(needs)):
                    needs[i] -= sp[i]
                if all(needs[i] >= 0 for i in range(len(needs))):
                    result = min(result, helper(needs[:]) + sp[-1])
                for i in range(len(needs)):
                    needs[i] += sp[i]
                d[tuple(needs)] = result
            return result
        n = max(needs) + 1
        m = len(needs)
        d = {}
        return helper(needs)