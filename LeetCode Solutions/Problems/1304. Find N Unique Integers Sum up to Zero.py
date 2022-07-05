class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        if n%2 != 0:
            arr.append(0)
        for i in range(n//2):
            arr.extend([-(i+1), (i+1)])
        return arr