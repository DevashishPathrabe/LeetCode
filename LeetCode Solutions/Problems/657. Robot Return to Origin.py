class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = collections.Counter(moves)
        if count["L"] != count["R"] or count["U"] != count["D"]:
            return False
        else:
            return True