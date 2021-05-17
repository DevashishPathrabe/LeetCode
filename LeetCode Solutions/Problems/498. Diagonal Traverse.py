class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        arr, diagonal = [],  collections.defaultdict(list)
        for idx, i in enumerate(mat):
            for jdx, j in enumerate(i):
                diagonal[idx+jdx] += [j]      
        for idx, row in enumerate(diagonal.values()):
            if(idx % 2 == 0):
                row.reverse()
            arr.extend(row)
        return arr