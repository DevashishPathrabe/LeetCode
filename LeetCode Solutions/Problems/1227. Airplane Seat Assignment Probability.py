class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return round(n, 5)
        return 0.50000