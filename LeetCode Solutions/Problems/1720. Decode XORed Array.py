class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [0] * (len(encoded) + 1)
        n = len(arr)
        arr[0] = first
        for i in range(1, n):
            arr[i] = encoded[i-1] ^ arr[i-1]
        return arr