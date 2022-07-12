class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rm=len(mat)
        cm=len(mat[0])
        out=[([0]*c) for i in range(r)]
        if rm*cm!=r*c:
            return mat
        p=0
        q=0
        for i in mat:
            for j in i:
                out[p][q]=j
                q+=1
                if q==c:
                    q=0
                    p+=1
        return out