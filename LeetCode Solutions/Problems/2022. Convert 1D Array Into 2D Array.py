class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if not n*m == len(original) :
            return []
        arr = []
        for i in range(0, len(original), n):
            arr.append(original[i:i+n])
        return arr