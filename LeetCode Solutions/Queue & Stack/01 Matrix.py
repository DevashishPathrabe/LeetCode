class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row, column = len(matrix), len(matrix[0])
        def helper(matrix, a, b):
            st = [[a,b,0]]
            while(st):
                m, n, s = st.pop(0)
                if(matrix[m][n] == 0): 
                    matrix[a][b] = s 
                    return 0
                for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                    j = m+x
                    k = n+y
                    if(0 <= j<row and 0 <= k<column):
                        st.append([j, k, s+1])
        for i in range(row):
            for j in range(column):
                if(matrix[i][j] == 1):
                    helper(matrix, i, j)
        return matrix