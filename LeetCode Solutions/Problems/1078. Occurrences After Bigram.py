class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        arr = []
        token = text.split(" ")
        for i in range(2, len(token)):
            if token[i-2] == first and token[i-1] == second:
                arr.append(token[i])
        return arr