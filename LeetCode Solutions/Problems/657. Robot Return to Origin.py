class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = collections.Counter(moves)
        if c["L"] != c["R"] or c["U"] != c["D"]:
            return False
        else:
            return True