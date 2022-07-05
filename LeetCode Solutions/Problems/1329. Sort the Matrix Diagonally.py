class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        N, M = len(mat), len(mat[0])
        def helper(i,j, data):
            if(i > N-1 or j > M-1):
                return sorted(data)
            else:
                sortedData = helper(i+1, j+1, data+[mat[i][j]])
                mat[i][j] = sortedData[-1]
                return sortedData[:-1]
        for j in range(len(mat[0])):
            out = helper(0,j,[])
        for i in range(len(mat)):
            out = helper(i,0,[])
        return mat