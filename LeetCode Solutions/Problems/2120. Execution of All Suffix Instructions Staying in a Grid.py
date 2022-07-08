class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res = [0]*len(s)
        for i in range(len(s)):
            x = startPos[0]
            y = startPos[1]
            steps = 0
            for j in range(i, len(s)):
                if s[j] == "U": 
                    x -= 1
                elif s[j] == "R":
                    y += 1
                elif s[j] == "L":
                    y -= 1
                else:
                    x += 1
                if self.isWithinGrid(x, y, n):
                    steps += 1
                else:
                    break
                res[i] = steps
        return res
    def isWithinGrid(self, x, y, n):
        if x >= 0 and x < n and y >= 0 and y < n:
            return True
        else:
            return False