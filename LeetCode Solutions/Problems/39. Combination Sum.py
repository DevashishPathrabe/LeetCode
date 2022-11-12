class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        dp = {}
        dp[0] = [[]]
        for candidate in sorted(candidates):
            for n in range(candidate, target + 1):
                combinations = dp.get(n - candidate, [])
                dp.setdefault(n, [])
                for combo in combinations:
                    dp[n].append(combo + [candidate])
        return dp.get(target, [])