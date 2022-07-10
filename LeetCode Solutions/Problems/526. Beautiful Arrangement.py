class Solution:
    def countArrangement(self, n: int) -> int:
        self.beautifulArrangements = 0
        def helper(i, cands):
            if(i <= 1):
                self.beautifulArrangements += 1
                return
            for j, x in enumerate(cands):
                if(i%x == 0 or x%i == 0):
                    helper(i-1, cands[:j] + cands[j+1:])
        helper(n, list(range(1, n+1)))
        return self.beautifulArrangements