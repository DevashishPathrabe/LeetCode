import numpy as np
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out, arr = [], np.array(matrix)
        while arr.size:
            out.append(arr[0])
            arr = arr[1:].T[::-1]
        return np.concatenate(out)