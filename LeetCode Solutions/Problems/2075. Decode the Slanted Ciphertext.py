class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        result = []
        cols = n // rows
        for i in range(cols):
            for j in range(i, n, cols+1):
                result.append(encodedText[j])
        return ''.join(result).rstrip(' ')