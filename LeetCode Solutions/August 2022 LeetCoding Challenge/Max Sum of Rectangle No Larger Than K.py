from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        M = len(matrix)
        N = len(matrix[0])
        CSr = [ None for _ in matrix]
        for i,row in enumerate(matrix):
            CSr[i] = list(accumulate(row, initial=0))
        best = float('-inf')
        for r1 in range(M):
            Srow = [0]*(N+1)
            for r2 in range(r1+1,M+1):
                Srow = [a+b for a,b in zip(Srow,CSr[r2-1])]
                SL = SortedList(Srow)
                for c in range(N):
                    target = k + Srow[c]
                    SL.remove(Srow[c])
                    j = SL.bisect(target)-1
                    if j<0:
                        continue
                    best = max(best, SL[j]-Srow[c])
        return best