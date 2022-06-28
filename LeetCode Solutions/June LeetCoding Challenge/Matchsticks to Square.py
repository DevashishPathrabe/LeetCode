class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks = sorted(matchsticks, reverse=True)
        N, S = len(matchsticks), sum(matchsticks)
        if(N < 4 or S % 4 or matchsticks[0] > S/4):
            return False
        side, taken = S/4, set()
        def helper(i: int, target: int) -> bool:
            if(i == N):
                return False
            if(i in taken):
                return helper(i + 1, target)
            current = matchsticks[i]
            if(current <= target):
                taken.add(i)
                if(current == target or helper(i+1, target - current)):
                    return True
                taken.remove(i)
            return helper(i+1, target)
        for _ in range(3):
            if(not helper(0, side)):
                return False
        return True